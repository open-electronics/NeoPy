# NeoPy
NeoPy is a way to control your NeoPixel LEDs via WiFi in Python.

## Hardware
- Fishino or NodeMCU
- (optional) Raspberry Pi

## Steps
1) Setup Fishino or NodeMCU sketch with your WiFi credentials and LEDs number and flash the sketch
2) Include neopy.py in your Python script to control LEDs over WiFi

## NeoPy.py usage
- Instance one NeoPy object with 90 LEDs, send commands to these IP and PORT:
```
    strip = NeoPy(90, "192.168.1.123", 4242)
```
- Set the third LED to RED:
```
    strip.Set(2, (255, 0, 0))
```
- Set all LEDs to blue:
```
    strip.SetAll((0, 0, 255))
```
- Set all LEDs half brightness (input values from 0 to 100):
```
    strip.SetBrightness(50)
```
- Retrieve one RGB color from Wheel (input values from 0 to 255) and set to all LEDs:
```
    color = strip.Wheel(128)
    strip.SetAll(color)
```
- LED matrix mode (True/False, Width, Height, First pixel position [TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT]):
```
    strip.IsMatrix(True, 12, 12, matrix.BOTTOM_LEFT)
```
- Set pixel color of a LED matrix (position 2,4 and colore green):
```
    strip.SetPixel(2, 4, (0, 255, 0))
```
- Refresh the strip (send command over WiFi):
```
    strip.Show()
```
