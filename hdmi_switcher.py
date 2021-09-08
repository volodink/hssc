import argparse
import serial
import time

parser = argparse.ArgumentParser(description='Serial HDMI switch command sender')

parser.add_argument('--port', type=str, help='Serial port, e.g. /dev/ttyUSB0')
parser.add_argument('--chan', type=str, help='Channel to be selected')

args = parser.parse_args()
print(args.port, args.chan)

try:
    with serial.Serial(args.port) as ser:
        command = f'{args.chan}\n'
        ser.write(command)
        time.sleep(0.05)
except serial.SerialException as e:
    print(e)

