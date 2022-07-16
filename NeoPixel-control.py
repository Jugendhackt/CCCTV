import board
import neopixel
import time
pixels = neopixel.NeoPixel(board.D18, 16)
while True:
    for ind in range(len(pixels)):
        if ind%2 == 1:
            pixels[ind] = (20, 10, 20)
        else:
            pixels[ind] = (0, 0, 0)
    pixels.show()
    time.sleep(0.5)
    for ind in range(len(pixels)):
        if ind%2 == 0:
            pixels[ind] = (20, 0, 20)
        else:
            pixels[ind] = (0, 0, 0)
    pixels.show()
    time.sleep(0.5)