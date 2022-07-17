from picamera import PiCamera
from time import sleep
import sys

camera = PiCamera()

if __name__ == '__main__':
    try:
        
        camera.capture(f'/tmp/pct/picture{sys.argv[1]}.jpg')
        camera.stop_preview()
        camera.close()
    except Exception as error:
        print(error)
        camera.close()
        exit()
