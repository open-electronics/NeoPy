"""
Description: Examples for NeoPixel 12x12 matrix
Product: 
Author: Luca Bellan
Version: 1.0
Date: 14-01-2019
"""


from neopy import NeoPy
import time, random


matrix = NeoPy(144, "192.168.1.8")
matrix.IsMatrix(True, 12, 12, matrix.BOTTOM_LEFT)

matrix.SetBrightness(90)


print("Hypnotic squares (20 times)")

for c in range(20):
    for i in range(6):
        color = matrix.Wheel(random.randrange(256))
        for x in range(i, matrix.w - i):
            matrix.SetPixel(x, i, color)
            matrix.SetPixel(x, matrix.h - 1 - i, color)
        for y in range(i, matrix.h - i):
            matrix.SetPixel(i, y, color)
            matrix.SetPixel(matrix.w - 1 - i, y, color)
        matrix.Show()
        time.sleep(0.05)



print("Spiral (10 times)")

for c in range(5):
    color = matrix.Wheel(random.randrange(256))
    for g in range(6):
        for i in range(g, matrix.w - g):
            matrix.SetPixel(i, g, color)
            matrix.Show()
            time.sleep(0.02)
        for i in range(g + 1, matrix.h - g):
            matrix.SetPixel(matrix.w - 1 - g, i, color)
            matrix.Show()
            time.sleep(0.02)
        for i in reversed(range(g, matrix.w - 1 - g)):
            matrix.SetPixel(i, matrix.h - 1 - g, color)
            matrix.Show()
            time.sleep(0.02)
        for i in reversed(range(g + 1, matrix.h - g - 1)):
            matrix.SetPixel(g, i, color)
            matrix.Show()
            time.sleep(0.02)



print("Crossing lines (15 times)")

for c in range(10):
    color1 = matrix.Wheel(random.randrange(256))
    color2 = matrix.Wheel(random.randrange(256))
    for col in range(matrix.w):
        for row in range(matrix.h):
            if row % 2 == 0:
                matrix.SetPixel(col, row, color1)
            else:
                matrix.SetPixel(matrix.w - 1 - col, row, color2)
        matrix.Show()
        time.sleep(0.05)
    for col in range(matrix.w):
        for row in range(matrix.h):
            if row % 2 == 0:
                matrix.SetPixel(col, row, (0, 0, 0))
            else:
                matrix.SetPixel(matrix.w - 1 - col, row, (0, 0, 0))
        matrix.Show()
        time.sleep(0.05)



print("Random color + random fill in (400 times)")

for c in range(400):
    x = random.randrange(matrix.w)
    y = random.randrange(matrix.h)
    matrix.SetPixel(x, y, matrix.Wheel(random.randrange(256)))
    matrix.Show()
    time.sleep(0.03)




print("Clock")

numbers = {}
numbers[0] = [(0,1,1,0), (1,0,0,1), (1,0,0,1), (1,0,0,1), (0,1,1,0)]
numbers[1] = [(0,1,1,0), (0,0,1,0), (0,0,1,0), (0,0,1,0), (0,1,1,1)]
numbers[2] = [(1,1,1,0), (0,0,0,1), (0,1,1,0), (1,0,0,0), (1,1,1,1)]
numbers[3] = [(1,1,1,0), (0,0,0,1), (0,1,1,0), (0,0,0,1), (1,1,1,0)]
numbers[4] = [(1,0,1,0), (1,0,1,0), (1,0,1,0), (1,1,1,1), (0,0,1,0)]
numbers[5] = [(1,1,1,1), (1,0,0,0), (1,1,1,0), (0,0,0,1), (1,1,1,0)]
numbers[6] = [(0,1,1,0), (1,0,0,0), (1,1,1,0), (1,0,0,1), (0,1,1,0)]
numbers[7] = [(1,1,1,1), (0,0,0,1), (0,0,1,0), (0,1,0,0), (0,1,0,0)]
numbers[8] = [(0,1,1,0), (1,0,0,1), (0,1,1,0), (1,0,0,1), (0,1,1,0)]
numbers[9] = [(0,1,1,0), (1,0,0,1), (0,1,1,1), (0,0,0,1), (0,1,1,0)]


color = (100, 100, 100)
orario = ""
while True:
    if orario != time.strftime("%H%M"):
        orario = time.strftime("%H%M")
        StartX = 0
        StartY = 0
        x = StartX
        y = StartY
        cont = 0
        matrix.SetAll((100, 0, 0))
        matrix.Show()
        for c in orario:
            if int(c) in numbers:
                y = StartY
                for row in numbers[int(c)]:
                    x = StartX + 5 * cont
                    for p in row:
                        if p == 1:
                            matrix.SetPixel(x, y, color)
                        x += 1
                    y += 1
                cont += 1
                if cont == 2:
                    StartY += 7
                    StartX = 3
                    cont = 0
        matrix.Show()




matrix.SetAll((0, 0, 0))
matrix.Show()
print("END")
