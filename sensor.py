#Bibliotheken einbinden
import RPi.GPIO as GPIO
import board
import neopixel
import os
import time
import recorder
import npc
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
BLACK = (0, 0, 0)

#Aufnahme
MAX_DIST = 150
LastTimeElapsed = 0
ImageCount = 1
Led = npc.LED(npc.RAINBOW)

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
    
    return distanz

    
    
if __name__ == '__main__':
    try:
        while True:
            Led.start()
            LastDist = Abstand
            Abstand = distanz()
            
            if Abstand < MAX_DIST:
                Led.set_state(1)
                
                if time.time() - LastTimeElapsed >= 5:
                    os.system(f"python recorder.py {ImageCount}")
                    if ImageCount > 5:
                        ImageCount = 0
                        
                    ImageCount+=1
                    print(f"Recording {ImageCount} saved")
                    LastTimeElapsed = time.time()
            else:
                Led.set_state(0)
                
                LastTimeElapsed = time.time() - 5
                
 
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
        GPIO.cleanup()
