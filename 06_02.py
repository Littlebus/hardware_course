import smbus
import time

address = 0x48
cmd = 0x40
bus = smbus.SMBus(1)

def ledu(u):
    bus.write_byte_data(address, cmd, u)

if __name__ == '__main__':
    while True:
        for i in range(0,0xff):
            ledu(i)
        