"""NeoPixel Controller
Library for controlling the NeoPixel LED Stripe
"""

# Import libraries
import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 16)
# pixels = [0 for _ in range(16)] ## Use for debugging

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

# Variables
ACTIVE = 1
PASSIVE = 0


class NeoPixel:
    """Class to control LED colors"""

    def __init__(self, active_color, passiv_color):
        # set initial vals
        self.count = 0
        self.passiv = self.color = active_color
        self.active = passiv_color
        self.recording = 0

    def set_state(self, recording):
        """Set LED colors"""
        self.recording = recording

        # set colors based on if recording
        if recording == 1:
            self.color = self.active
        else:
            self.color = self.passiv

    def show(self):
        """Display LED"""

        # Reset count if bigger than the number of available colors
        if self.count >= len(self.color):
            self.count = 0

        # Set each LED Pixel individually
        for ind in range(len(pixels)):
            pixels[ind] = self.color[(ind + self.count) % len(self.color)]

        pixels.show()

        # Increment count
        self.count += 1

        # Blink faster if recording
        if self.recording:
            time.sleep(0.025)
        else:
            time.sleep(0.2)


if __name__ == "__main__":
    led = NeoPixel([RED, ORANGE] * 8, RAINBOW)
    count = 0
    while True:
        led.show()

        # Switch state every 15 runs
        if (count / 15) % 1 <= 0.5:
            led.set_state(PASSIVE)
        else:
            led.set_state(ACTIVE)

        count += 1
