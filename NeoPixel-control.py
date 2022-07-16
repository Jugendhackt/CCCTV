import board
import neopixel
import time
from collections import deque

pixels = neopixel.NeoPixel(board.D18, 16)
# pixels = [0 for _ in range(16)]

BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 127, 0)
RAINBOW = [
    (255, 127, 0),
    (127, 255, 0),
    (37, 63, 180),
    (164, 63, 116),
    (127, 127, 0),
    (201, 63, 105),
    (255, 63, 0),
    (255, 191, 0),
    (0, 127, 127),
    (74, 0, 233),
    (255, 0, 0),
    (255, 127, 0),
    (255, 255, 0),
    (0, 255, 0),
    (0, 0, 255),
    (202, 64, 106),
]


class LED:
    def __init__(self, rainbow):
        self.count = 0
        self.rainbow = rainbow
        self.colors = [RED, ORANGE] * 8

    def change_state(self, recording):
        if recording == 1:
            self.colors = [RED, ORANGE]
        else:
            self.colors = self.rainbow
        # print("Colors", self.colors)

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
            pixels[ind] = self.colors[(ind + self.count) % len(self.colors)]
        self.count += 1
        time.sleep(1)
        print(pixels)


if __name__ == "__main__":
    led = LED(RAINBOW)
    count = 0
    while True:
        led.start()
        if (count / 10) % 1 <= 0.5:
            led.change_state(0)
        else:
            led.change_state(1)

        count += 1
