"""
Description: Examples for NeoPixel 150 LEDs strip
Product: https://www.futurashop.it/NEOPIXEL_STRIP_RGB_STRIP150LED
Author: Luca Bellan
Version: 1.0
Date: 11-01-2019
"""


from neopy import NeoPy
import time, random


strip = NeoPy(150, "192.168.1.9")


print("Sparkling white (300 times)")

strip.SetBrightness(100)
for c in range(300):
    strip.SetAll((10, 10, 10))
    pixel = random.randrange(strip.NumPixels())
    strip.Set(pixel, (255, 255, 255))
    strip.Show()
    time.sleep(0.03)
    strip.Set(pixel, (180, 180, 180))
    strip.Show()
    time.sleep(0.03)




print("Running rainbow (5 times)")

strip.SetBrightness(70)
conv = 256 / strip.NumPixels()
for c in range(5):
    for j in range(strip.NumPixels()):
        for i in range(strip.NumPixels()):
            loc = (i+j) % strip.NumPixels()
            wh = strip.Wheel(loc * conv)
            strip.Set(i,wh)
        strip.Show()
        time.sleep(0.04)




print("Color fade (3 times)")

strip.SetBrightness(50)
for c in range(3):
    for i in range(256):
        for j in range(strip.NumPixels()):
            strip.SetAll(strip.Wheel(i))
        strip.Show()
        time.sleep(0.02)




print("KITT supercar (3 times)")

strip.SetBrightness(70)
for c in range(5):
    for i in range(strip.NumPixels() - 5):
        strip.SetAll((0, 0, 0))
        strip.Set(i, (25, 0, 0))
        for j in range(1, 5):
            strip.Set(i+j, (255, 0, 0))
        strip.Set(i+5, (255, 0, 0))
        strip.Show()
        time.sleep(0.03)
    time.sleep(0.04)
    for i in reversed(range(0, strip.NumPixels()-6)):
        strip.SetAll((0, 0, 0))
        strip.Set(i, (25, 0, 0)) 
        for j in range(1, 5):
            strip.Set(i+j, (255, 0, 0))
        strip.Set(i+5, (25, 0, 0))
        strip.Show()
        time.sleep(0.03)
    time.sleep(0.04)




print("Fill and wipe colors (1 time)")

ColorPos = 0
for j in range(5):
    for i in range(strip.NumPixels()):
        strip.Set(i, strip.Wheel(ColorPos))
        strip.Show()
        time.sleep(0.02)
    for i in range(strip.NumPixels()):
        strip.Set(i, (0, 0, 0))
        strip.Show()
        time.sleep(0.01)
    ColorPos += 50



print("Collision and explosion (5 times)")

for c in range(5):
    strip.SetBrightness(90)
    num = strip.NumPixels()
    middle = 0
    white = 255
    for i in range(num):
        strip.SetAll((0, 0, 0))
        strip.Set(i, (255, 0, 0))
        strip.Set(num-i-1, (0, 0, 255))
        strip.Show()
        time.sleep(0.03)
        if i == (num-i-1):
            middle = i
            break
    for i in range(int(middle * 0.9)):
        strip.Set(middle - i, (white, white, white))
        strip.Set(middle + i, (white, white, white))
        strip.Show()
        time.sleep(0.02)
        white -= 6
    for i in reversed(range(60)):
        strip.SetBrightness(i)
        strip.Show()
        time.sleep(0.02)



strip.SetAll((0, 0, 0))
strip.Show()
print("END")

