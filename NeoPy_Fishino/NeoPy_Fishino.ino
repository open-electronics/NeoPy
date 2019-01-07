/*
Name: NeoPy - Fishino
Description: NeoPixels UDP controller
Author: Luca Bellan
Version: 1.3
Date: 04-01-2019
*/

#include <Fishino.h>
#include <SPI.h>
#include <Adafruit_NeoPixel.h>

//      BEGIN SETUP
#define MY_SSID	"mio_ssid"
#define MY_PASS	"mia_password"
#define LEDS 56
//#define IPADDR  192, 168, 1, 19
#define GATE  192, 168, 1, 1
#define SUB  255, 255, 255, 0
#define PORT  4242
#define PIN 3
//      END SETUP

FishinoUDP Udp;
Adafruit_NeoPixel strip = Adafruit_NeoPixel(LEDS, PIN, NEO_GRB + NEO_KHZ800);
#ifdef IPADDR
  IPAddress ip(IPADDR);
  IPAddress gateway(GATE);
  IPAddress subnet(SUB);
#endif

long unsigned int packetSize;
unsigned int len;
int r, g, b;

void setup() {

	while(!Fishino.reset()) {
   delay(500);
  }
	Fishino.setMode(STATION_MODE);
	while(!Fishino.begin(MY_SSID, MY_PASS)) {
		delay(500);
	}
  #ifdef IPADDR
    Fishino.config(ip, gateway, subnet);
  #else
    Fishino.staStartDHCP();
  #endif
	while(Fishino.status() != STATION_GOT_IP) {
		delay(500);
	}
 
	Udp.begin(PORT);

  strip.begin();
  strip.show();
 
}




void loop() {

  packetSize = Udp.parsePacket();
  if (packetSize == LEDS * 3) {
    char packetBuffer[packetSize];
    len = Udp.read(packetBuffer, packetSize);
    if (len > 0) {
      packetBuffer[len] = 0;
    }
    for (int i=0; i<LEDS * 3; i+=3) {
        r = (int)(byte*)(packetBuffer)[i];
        g = (int)(byte*)(packetBuffer)[i+1];
        b = (int)(byte*)(packetBuffer)[i+2];
        strip.setPixelColor(i/3, r, g, b);
    }
    strip.show();
  }

}

