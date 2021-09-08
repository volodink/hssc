import argparse
from turtle import speed
import serial
import time

parser = argparse.ArgumentParser(description='Serial HDMI switch command sender')

parser.add_argument('--port', type=str, help='Serial port, e.g. /dev/ttyUSB0')
parser.add_argument('--chan', type=str, help='Channel to be selected')

args = parser.parse_args()

try:
    with serial.Serial(args.port, 19200, timeout=1) as ser:
        command = f'I{args.chan}\n'.encode('utf-8')
        ser.write(command)
        time.sleep(0.05)
except serial.SerialException as e:
    print(e)

