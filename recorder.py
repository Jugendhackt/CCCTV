from picamera import PiCamera
from time import sleep
import sys

if __name__ == '__main__':
    try:
        PiCamera().capture(f'/tmp/picture{sys.argv[1]}.jpg')
    except:
       exit()
