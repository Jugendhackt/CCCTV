from picamera import PiCamera
from time import sleep
camera = PiCamera()

def record(arg):
    sleep(2)
    camera.capture(f'/tmp/picture{arg}.jpg')
    
