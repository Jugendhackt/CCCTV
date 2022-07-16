import board
import neopixel
import time
from collections import deque

pixels = neopixel.NeoPixel(board.D18, 16)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
VIOLET = (238, 130, 238)


class LED:
    def __init__(self):
        self.count = 0
        self.colors = [(20, 100, 20), (100, 50, 20)]

    def change_state(self, recording):
        if recording == 1:
            self.colors = [RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET]
        else:
            self.colors = [RED, ORANGE]

    # def start(self):
    #     for ind in range(len(pixels)):
    #         if ind % 2 == 1:
    #             pixels[ind] = self.colors[0]
    #         else:
    #             pixels[ind] = BLACK
    #     pixels.show()
    #     time.sleep(1)
    #     for ind in range(len(pixels)):
    #         if ind % 2 == 0:
    #             pixels[ind] = self.colors[1]
    #         else:
    #             pixels[ind] = BLACK
    #     pixels.show()
    #     time.sleep(1)

    def start(self):
        if self.count >= len(self.colors):
            self.count = 0
        for ind in range(len(pixels)):
            if ind % len(self.colors) == 0:
                pixels[ind] = deque(self.colors[ind % len(self.colors)]).rotate(
                    self.count
                )
        self.count += 1
        time.sleep(1)


if __name__ == "__main__":
    led = LED()
    count = 0
    while True:
        led.start()
        # led.change_state(count % 5)
        count += 1
