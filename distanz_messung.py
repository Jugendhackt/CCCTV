#Bibliotheken einbinden
import RPi.GPIO as GPIO
import board
import neopixel
import time
 import os
#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#GPIO Pins zuweisen
GPIO_TRIGGER = 25
GPIO_ECHO = 12

#Distanz Tracker
LastDist = 0.0
Abstand = 0.0

#Visualisierung
pixels = neopixel.NeoPixel(board.D18, 16)
RenderDistance = 0
BLACK = (0, 0, 0)

#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distanz():
    # setze Trigger auf HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # setze Trigger nach 0.01ms aus LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartZeit = time.time()
    StopZeit = time.time()
 
    # speichere Startzeit
    while GPIO.input(GPIO_ECHO) == 0:
        StartZeit = time.time()
 
    # speichere Ankunftszeit
    while GPIO.input(GPIO_ECHO) == 1:
        StopZeit = time.time()
 
    # Zeit Differenz zwischen Start und Ankunft
    TimeElapsed = StopZeit - StartZeit
    # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
    # und durch 2 teilen, da hin und zurueck
    distanz = (TimeElapsed * 34300) / 2
    
    if distanz > 500:
        print("gemessene zeit: %.5f" % TimeElapsed)
    return distanz
 
if __name__ == '__main__':
    try:
        while True:
            LastDist = Abstand
            Abstand = distanz()
            if abs(Abstand - LastDist) >= 160: Abstand = LastDist
            print ("Gemessene Entfernung = %.1f cm" % Abstand)
            print ("Differenz zur letzten Distanz: %.1f cm" % abs(Abstand - LastDist))
            RenderDistance = int(Abstand / 10)
            for i in range(16):
                if i <= RenderDistance:
                    pixels[i] = ([100, 0, 100])
                else:
                    pixels[i] = ([0, 0, 0])
                    
            pixels.show()
            time.sleep(0.1)
 
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
        GPIO.cleanup()
