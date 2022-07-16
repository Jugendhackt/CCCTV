import board
import neopixel
import time
from collections import deque

pixels = neopixel.NeoPixel(board.D18, 16)
# pixels = [0 for _ in range(16)]

BLACK = (0, 0, 0)
RED = (127, 0, 0)
ORANGE = (127, 63, 0)
RAINBOW = [
    (127, 63, 0),
    (63, 127, 0),
    (18, 31, 90),
    (82, 31, 58),
    (63, 63, 0),
    (100, 31, 52),
    (127, 31, 0),
    (127, 95, 0),
    (0, 63, 63),
    (37, 0, 116),
    (127, 0, 0),
    (127, 63, 0),
    (127, 127, 0),
    (0, 127, 0),
    (0, 0, 127),
    (101, 32, 53),
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
