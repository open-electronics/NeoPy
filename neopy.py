"""
Name: NeoPy
Description: This class allow UDP communication between Python and NodeMCU/Fishino for NeoPixels control
Author: Luca Bellan
Version: 1.3
Date: 14-01-2019
"""


import socket
import time
import random
import math


class NeoPy():

    def __init__(self, leds=0, ip = "127.0.0.1", port = 4242, ledsPerPacket=128):
        self.strip = [(0, 0, 0) for i in range(leds)]
        self.brightness = 80
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.matrix = False
        self.number = 1
        self.w = 1
        self.h = 1
        self.TOP_LEFT = 0
        self.TOP_RIGHT = 1
        self.BOTTOM_LEFT = 2
        self.BOTTOM_RIGHT = 3
        self.startled = self.TOP_LEFT
        self.ip = ip
        self.port = port
        self.ledsPerPacket = ledsPerPacket
        self.Show()

    def IsMatrix(self, mode = False, number = 1, w = 1, h = 1, start = 0):
        if start in [0, 1, 2, 3] and w > 0 and h > 0:
            self.matrix = mode
            self.startled = start
            self.number = number
            self.w = w
            self.h = h

    def Set(self, index, color):
        if index >= 0 and index <= len(self.strip):
            self.strip[index] = color           

    def SetPixel(self, x, y, color):
        if self.matrix and x < (self.w * self.number) and y < self.h:
            matr = math.floor(x / self.w)
            if self.startled == self.TOP_RIGHT:
                oldx = x
                x = y
                y = self.w - oldx - 1
            elif self.startled == self.BOTTOM_LEFT:
                oldx = x
                x = self.w - y - 1
                y = oldx
            elif self.startled == self.BOTTOM_RIGHT:
                x = self.w - x - 1
                y = self.w - y - 1
            pos = y * self.w + x
            if y % 2:
                pos = y * self.w + (self.w - x - 1)
            self.Set(pos, color)

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
        numleds = len(self.strip)
        packetNo = 0
        i = 0
        while i < numleds:
            seq = []
            seq.append(packetNo)
            while i < min((packetNo+1)*self.ledsPerPacket, numleds):
                seq.append(int(self.strip[i][0] * self.brightness / 100))
                seq.append(int(self.strip[i][1] * self.brightness / 100))
                seq.append(int(self.strip[i][2] * self.brightness / 100))
                i += 1
            self.sock.sendto(bytearray(seq), (self.ip, self.port))
            packetNo += 1
