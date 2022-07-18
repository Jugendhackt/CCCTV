# Import Libraries
import RPi.GPIO as GPIO
import board
import neopixel
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# Set GPIO Pins
GPIO_TRIGGER = 25
GPIO_ECHO = 12

# Distance Tracker
LastDist = 0.0
Distance = 0.0

# Visualization
pixels = neopixel.NeoPixel(board.D18, 16)
RenderDistance = 0
BLACK = (0, 0, 0)
LILAC = (100, 0, 100)

# Set Directions of the GPIO-Pins (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def get_distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger to LOW after 0.01ms
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save starting time
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save end time
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # Difference between start and end time
    TimeElapsed = StopTime - StartTime
    # multiply with the velocity of sound (34300 cm/s)
    # divide by two, the away and back way
    dist = (TimeElapsed * 34300) / 2

    return dist


if __name__ == "__main__":
    try:
        while True:
            LastDist = Distance
            Distance = get_distance()
            if abs(Distance - LastDist) >= 160:
                Distance = LastDist
            print("Measured Distance: %.1f cm" % Distance)
            print("Difference to last Distance: %.1f cm" % abs(Distance - LastDist))
            RenderDistance = int(Distance / 10)
            for i in range(16):
                if i <= RenderDistance:
                    pixels[i] = LILAC
                else:
                    pixels[i] = BLACK

            pixels.show()
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Measuring was Aborted by User")
        GPIO.cleanup()
