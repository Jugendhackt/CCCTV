import board
import neopixel
import time
from collections import deque

pixels = neopixel.NeoPixel(board.D18, 16)
# pixels = [0 for _ in range(16)]

# Color Codes
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
    """Class to control LED colors"""

    def __init__(self, rainbow):
        self.count = 0
        self.rainbow = rainbow
        self.colors = [RED, ORANGE] * 8
        self.recording = 0

    def set_state(self, recording):
        """Change LED colors"""
        self.recording = recording
    
        if recording == 1:
            self.colors = [RED, ORANGE] * 8
        else:
            self.colors = self.rainbow

    def start(self):
        """Change LED colors"""
        if self.count >= len(self.colors):
            self.count = 0
        for ind in range(len(pixels)):
            pixels[ind] = self.colors[(ind + self.count) % len(self.colors)]
        self.count += 1
        if self.recording:
            time.sleep(0.025)
        else:
            time.sleep(0.2)


if __name__ == "__main__":
    led = LED(RAINBOW)
    count = 0
    while True:
        led.start()
        if (count / 15) % 1 <= 0.5:
            led.set_state(0)
        else:
            led.set_state(1)

        count += 1
