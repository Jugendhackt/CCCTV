# Import Libraries
import RPi.GPIO as GPIO
import os
import time
import npc
import subprocess
import distance

dir = "/tmp/pct"
if not os.path.exists(dir):
    os.mkdir(dir)


# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# Set GPIO Pins
GPIO_TRIGGER = 25
GPIO_ECHO = 12

# Distance Tracker
LastDist = 0.0
Distance = 0.0

# Recording
MAX_DIST = 150
MAX_IMAGES = 6
LastTimeElapsed = 0
ImageCount = 1
led = npc.NeoPixel([npc.RED, npc.ORANGE] * 8, npc.RAINBOW)

# Set Directions of the GPIO-Pins (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


if __name__ == "__main__":
    try:
        while True:
            led.show()
            LastDist = Distance
            Distance = distance.get_distance()

            if Distance < MAX_DIST:
                led.set_state(npc.ACTIVE)

                if time.time() - LastTimeElapsed >= 5:
                    p = subprocess.run(["python", "camera.py", f"{ImageCount}"])
                    if ImageCount > MAX_IMAGES - 1:
                        ImageCount = 0

                    print(f"Image {ImageCount} saved")
                    ImageCount += 1
                    LastTimeElapsed = time.time()
            else:
                led.set_state(npc.PASSIVE)

                LastTimeElapsed = time.time() - 5

    except KeyboardInterrupt:
        print("Measuring was Aborted by User")
        GPIO.cleanup()
