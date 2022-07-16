import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 16)
BLACK = (0, 0, 0)


class LED:
    def __init__(self):
        self.colors = [(20, 100, 20), (100, 50, 20)]

    def change_state(self, recording):
        if recording == 1:
            self.colors = [(100, 20, 20), (100, 100, 20)]
        else:
            self.colors = [(20, 100, 20), (100, 50, 20)]

    def start(self):
        for ind in range(len(pixels)):
            if ind % 2 == 1:
                pixels[ind] = self.colors[0]
            else:
                pixels[ind] = (0, 0, 0)
        pixels.show()
        time.sleep(0.5)
        for ind in range(len(pixels)):
            if ind % 2 == 0:
                pixels[ind] = self.colors[1]
            else:
                pixels[ind] = (0, 0, 0)
        pixels.show()
        time.sleep(0.5)


if __name__ == "__main__":
    led = LED()
    count = 0
    while True:
        led.start()
        led.change_state(count % 5)
        count += 1
