"""
Description: Examples for NeoPixel star
Product: https://store.open-electronics.org/FT1300M-CHRISTMAS-STAR-WITH-LED-NEOPIXEL
Author: Luca Bellan
Version: 1.0
Date: 10-01-2019
"""


from neopy import NeoPy
import time, random


star = NeoPy(56, "192.168.1.8")


print("Sparkling white star (300 times)")

star.SetBrightness(100)
for c in range(300):
    star.SetAll((10, 10, 10))
    pixel = random.randrange(star.NumPixels())
    star.Set(pixel, (255, 255, 255))
    star.Show()
    time.sleep(0.03)
    star.Set(pixel, (180, 180, 180))
    star.Show()
    time.sleep(0.03)




print("Running rainbow (5 times)")

star.SetBrightness(70)
conv = 256 / star.NumPixels()
for c in range(5):
    for j in range(star.NumPixels()):
        for i in range(star.NumPixels()):
            loc = (i+j) % star.NumPixels()
            wh = star.Wheel(loc * conv)
            star.Set(i,wh)
        star.Show()
        time.sleep(0.04)




print("Color fade (3 times)")

star.SetBrightness(50)
for c in range(3):
    for i in range(256):
        for j in range(star.NumPixels()):
            star.SetAll(star.Wheel(i))
        star.Show()
        time.sleep(0.02)




print("Random color + random fill in (300 times)")

star.SetBrightness(50)
for c in range(300):
    pos = random.randrange(star.NumPixels())
    star.Set(pos, star.Wheel(random.randrange(256)))
    star.Show()
    time.sleep(0.03)




print("Dot + internal star + external star flashing (20 times)")

star.SetBrightness(50)
for c in range(20):
    color = star.Wheel(random.randrange(256))
    star.Set(55, color)
    star.Show()
    time.sleep(0.3)
    color = star.Wheel(random.randrange(256))
    for i in range(35, 55):
        star.Set(i, color)
    star.Show()
    time.sleep(0.3)
    color = star.Wheel(random.randrange(256))
    for i in range(35):
        star.Set(i, color)
    star.Show()
    time.sleep(0.3)


star.SetAll((0, 0, 0))
star.Show()
print("END")

