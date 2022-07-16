# CCCTV
A privacy-focused security camera which starts recording on movement.
The LEDs lets the person know that they're being recorded

## Requirements:
  - Power cable
  - RPI4 (2GB recommended)
  - Jumper Wire
  - Breadboard
  - Resistor (330Ω, 440Ω)
  - Camera (V2.1)
  - NeoPixel
  - Ultrasonic sensor (HC SR04)

## Files
- sensor.py
  - Main file of the project. Controls the hardware.
- distanz_messung.py
  - Meeasures the distance to object using the ultrasonic sensors.
- camera.py
  - Captures photos 
- recorder.py
  - Captures Videos
- npc.py
  - Neo Pixel Controller. Regulates the LED stripes.
- email.py
  - File to send emails
