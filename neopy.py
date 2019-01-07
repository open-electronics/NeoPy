"""
Name: NeoPy
Description: This class allow UDP communication between Python and NodeMCU/Fishino for NeoPixels control
Author: Luca Bellan
Version: 1.2
Date: 03-01-2019
USAGE
    - Instance one NeoPy object with 90 LEDs, send commands to these IP and PORT:
        strip = NeoPy(90, "192.168.1.123", 4242)
    - Set the third LED to RED:
        strip.Set(2, (255, 0, 0))
    - Set all LEDs to blue:
        strip.SetAll((0, 0, 255))
    - Set all LEDs half brightness (input values from 0 to 100):
        strip.SetBrightness(50)
    - Retrieve one RGB color from Wheel (input values from 0 to 255) and set to all LEDs:
        color = strip.Wheel(128)
        strip.SetAll(color)
    - Refresh the strip:
        strip.Show()
"""


import socket
import time
import random


class NeoPy():

    def __init__(self, leds=0, ip = "127.0.0.1", port = 4242):
        self.strip = [(0, 0, 0) for i in range(leds)]
        self.brightness = 80
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ip = ip
        self.port = port
        self.Show()

    def Set(self, index, color):
        if index >= 0 and index <= len(self.strip):
            self.strip[index] = color

    def SetAll(self, color):
        for i in range(len(self.strip)):
            self.Set(i, color)

    def SetBrightness(self, value):
        if value >= 0 and value <= 100:
            self.brightness = value

    def Wheel(self, position):
        position = 255 - position;
        if(position < 85):
            return (255 - position * 3, 0, position * 3);
        if(position < 170):
            position -= 85;
            return (0, position * 3, 255 - position * 3);
        position -= 170;
        return (position * 3, 255 - position * 3, 0);

    def NumPixels(self):
        return len(self.strip)
    
    def Show(self):
        seq = []
        for i in range(len(self.strip)):
            seq.append(int(self.strip[i][0] * self.brightness / 100))
            seq.append(int(self.strip[i][1] * self.brightness / 100))
            seq.append(int(self.strip[i][2] * self.brightness / 100))
        self.sock.sendto(bytearray(seq), (self.ip, self.port))

