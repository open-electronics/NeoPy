/*
Name: NeoPy - Fishino
Description: NeoPixels UDP controller
Author: Luca Bellan
Version: 1.5
Date: 23-02-2019
*/



#include <Fishino.h>
#include <SPI.h>
#include <Adafruit_NeoPixel.h>

//      BEGIN SETUP
#define MY_SSID  "mio_ssid"
#define MY_PASS "mia_password"
#define LEDS 56
//#define IPADDR  192, 168, 1, 19
#define GATE  192, 168, 1, 1
#define SUB  255, 255, 255, 0
#define PORT  4242
#define PIN 3
//      END SETUP

#define LPP 128
#define RES LEDS % LPP

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
char packetBuffer[LPP*3];

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
  if (packetSize == LPP * 3 + 1 || packetSize == RES * 3 + 1) {
    
    len = Udp.read(packetBuffer, packetSize);
    if (len > 0) {
      packetBuffer[len] = 0;
    }

    byte segmentNo = (int)(byte*)(packetBuffer)[0];  
    int from = segmentNo * LPP;

    for (int i=1; i<len; i+=3) {
        r = (int)(byte*)(packetBuffer)[i];
        g = (int)(byte*)(packetBuffer)[i+1];
        b = (int)(byte*)(packetBuffer)[i+2];
        strip.setPixelColor((i-1)/3 + from, strip.Color(r, g, b));
    }
    strip.show();
  }

}

