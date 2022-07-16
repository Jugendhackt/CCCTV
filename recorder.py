from picamera import PiCamera
from time import sleep
import sys

if __name__ == '__main__':
    try:
        PiCamera().start_recording(f'/tmp/picture{sys.argv[1]}.h264')
        sleep(5)
        piCamera().stop_recording()
    except:
       exit()