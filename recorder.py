from picamera import PiCamera
from time import sleep
import sys

if __name__ == '__main__':
    try:
        PiCamera().start_recording(f'/tmp/recording{sys.argv[1]}.h264')
        PiCamera().wait_recording(5)
        PiCamera().stop_recording()
        print(sys.argv[1])
        PiCamera().close()
    except Exception as error:
        print(error)
        PiCamera().close()
        exit()