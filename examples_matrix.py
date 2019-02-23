"""
Description: Examples for NeoPixel 12x12 matrix
Product: 
Author: Luca Bellan
Version: 1.5
Date: 23-02-2019
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

icons = {}
icons["sun"] = [(0, 0, 0, 0, 0, 0),
                (0, 1, 1, 1, 1, 0),
                (0, 1, 1, 1, 1, 0),
                (0, 1, 1, 1, 1, 0),
                (0, 1, 1, 1, 1, 0),
                (0, 0, 0, 0, 0, 0)]
icons["cloud"]=[(0, 0, 0, 0, 0, 0),
                (0, 0, 1, 1, 0, 0),
                (0, 1, 1, 1, 0, 0),
                (1, 1, 1, 1, 1, 0),
                (1, 1, 1, 1, 1, 1),
                (0, 0, 0, 0, 0, 0)]
icons["rain"] =[(0, 0, 1, 1, 0, 0),
                (0, 1, 1, 1, 1, 0),
                (1, 1, 1, 1, 1, 1),
                (0, 0, 0, 0, 0, 0),
                (1, 0, 1, 0, 1, 0),
                (0, 0, 0, 0, 0, 0)]
icons["snow"] = [(0, 0, 0, 0, 0, 0),
                (0, 0, 1, 0, 1, 0),
                (0, 1, 0, 1, 0, 1),
                (0, 0, 1, 1, 1, 0),
                (0, 1, 0, 1, 0, 1),
                (0, 0, 1, 0, 1, 0)]
icons["fog"] = [(0, 0, 0, 0, 0, 0),
                (0, 1, 1, 1, 1, 0),
                (0, 0, 0, 0, 0, 0),
                (0, 1, 1, 1, 1, 0),
                (0, 0, 0, 0, 0, 0),
                (0, 1, 1, 1, 1, 0)]




matrix = NeoPy(144, "192.168.1.8")
matrix.IsMatrix(True, 1, 12, 12, matrix.BOTTOM_LEFT)

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


while True:
    matrix.SetAll((0, 0, 70))
    DrawString(time.strftime("%H"), 2, 0, (100, 100, 100))
    DrawString(time.strftime("%M"), 2, 7, (100, 100, 100))
    matrix.Show()
    time.sleep(1)




print("Weather")

def DrawIcon(icon, x, y, color):
    if icon in icons:
        Relative_x = x
        Relative_y = y
        for row in icons[icon]:
            Relative_x = x
            for cell in row:
                if cell == 1:
                    matrix.SetPixel(Relative_x, Relative_y, color)
                Relative_x += 1
            Relative_y += 1


import pyowm

owm = pyowm.OWM("YOUR_API_KEY")
observation = owm.weather_at_place("milano,IT")

while True:
    w = observation.get_weather()
    matrix.SetAll((0, 0, 30))
    temp = str(int(w.get_temperature("celsius")["temp"])) + "°"
    DrawString(temp, 0, 0, (100, 100, 100))
    icon = w.get_weather_icon_name()
    #   Sole
    if icon in ["01d", "01n"]:
        color = (100, 100, 0)
        DrawIcon("sun", 3, 6, color)
    #   Nuvole
    elif icon in ["02d", "03d", "04d", "02n", "03n", "04n"]:
        color = (100, 100, 100)
        DrawIcon("cloud", 3, 6, color)
    #   Pioggia
    elif icon in ["09d", "10d", "11d", "09n", "10n", "11n"]:
        color = (10, 10, 250)
        DrawIcon("rain", 3, 6, color)
    #   Neve
    elif icon in ["13d", "13n"]:
        color = (100, 100, 100)
        DrawIcon("snow", 3, 6, color)
    #   Nebbia
    elif icon in ["50d", "50n"]:
        color = (100, 100, 100)
        DrawIcon("fog", 3, 6, color)
    matrix.Show()
    time.sleep(30)



matrix.SetAll((0, 0, 0))
matrix.Show()
print("END")
