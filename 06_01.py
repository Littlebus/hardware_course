import smbus
import time

address = 0x48
A0 = 0x40
bus = smbus.SMBus(1)

def readu():
    bus.write_byte(address, A0)
    value = bus.read_byte(address)
    return value

if __name__ == '__main__':
    while True:
        print readu()

