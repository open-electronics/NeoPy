"""
Description: Examples for NeoPixel 12x12 matrix
Product: 
Author: Luca Bellan
Version: 1.0
Date: 17-01-2019
"""


from neopy import NeoPy
import time, random


symbols = {}
symbols["0"] = [(1,1,1), (1,0,1), (1,0,1), (1,0,1), (1,1,1)]
symbols["1"] = [(0,1,0), (0,1,0), (0,1,0), (0,1,0), (0,1,0)]
symbols["2"] = [(1,1,1), (0,0,1), (1,1,1), (1,0,0), (1,1,1)]
symbols["3"] = [(1,1,1), (0,0,1), (0,1,1), (0,0,1), (1,1,1)]
symbols["4"] = [(1,0,1), (1,0,1), (1,1,1), (0,0,1), (0,0,1)]
symbols["5"] = [(1,1,1), (1,0,0), (1,1,1), (0,0,1), (1,1,1)]
symbols["6"] = [(1,1,1), (1,0,0), (1,1,1), (1,0,1), (1,1,1)]
symbols["7"] = [(1,1,1), (0,0,1), (0,0,1), (0,0,1), (0,0,1)]
symbols["8"] = [(1,1,1), (1,0,1), (1,1,1), (1,0,1), (1,1,1)]
symbols["9"] = [(1,1,1), (1,0,1), (1,1,1), (0,0,1), (1,1,1)]
symbols[":"] = [(0,0,0), (0,1,0), (0,0,0), (0,1,0), (0,0,0)]
symbols["/"] = [(0,0,0), (0,0,1), (0,1,0), (1,0,0), (0,0,0)]




matrix = NeoPy(144, "192.168.1.8")
matrix.IsMatrix(True, 12, 12, matrix.BOTTOM_LEFT)

matrix.SetBrightness(80)



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

for c in range(10):
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

for c in range(15):
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



orario = ""
while True:
    if orario != time.strftime("%H%M"):
        orario = time.strftime("%H%M")
        StartX = 0
        StartY = 0
        x = StartX
        y = StartY
        cont = 0
        matrix.SetAll((0, 0, 100))
        matrix.Show()
        for c in orario:
            if c in symbols:
                y = StartY
                for row in symbols[c]:
                    x = StartX + 4 * cont
                    for p in row:
                        if p == 1:
                            matrix.SetPixel(x, y, (100, 100, 100))
                        x += 1
                    y += 1
                cont += 1
                if cont == 2:
                    StartY += 7
                    StartX = 5
                    cont = 0
        matrix.Show()





print("Date and time")
                    
def DrawString(string, x, y, color):
    cont = 0
    for c in string:
        if c in symbols:
            Relative_x = x
            Relative_y = y
            if Relative_x + 2 <= 11:
                for row in symbols[c]:
                    Relative_x = x + 4 * cont
                    for cell in row:
                        if cell == 1:
                            matrix.SetPixel(Relative_x, Relative_y, color)
                        Relative_x += 1
                    Relative_y += 1
                cont += 1

Time_pos_x = 11
Time_pos_y = 0
Date_pos_x = 11
Date_pos_y = 7
while True:
    for r in range(12):
        for c in range(6):
            matrix.SetPixel(r, c, (0, 0, 100))
        for c in range(5, 7):
            matrix.SetPixel(r, c, (0, 100, 0))
        for c in range(7, 12):
            matrix.SetPixel(r, c, (100, 0, 0))
    matrix.Show()
    Time = time.strftime("%H:%M")
    Date = time.strftime("%d/%m/%Y")
    Time_pos_x -= 1
    if Time_pos_x < len(Time) * -4:
        Time_pos_x = 11
    DrawString(Time, Time_pos_x, Time_pos_y, (100, 100, 100))
    Date_pos_x -= 1
    if Date_pos_x < len(Date) * -4:
        Date_pos_x = 11
    DrawString(Date, Date_pos_x, Date_pos_y, (100, 100, 100))
    matrix.Show()
    time.sleep(0.3)



                      



matrix.SetAll((0, 0, 0))
matrix.Show()
print("END")
