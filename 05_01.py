import smbus
import time
import datetime

address = 0x68
register = 0x00
bus = smbus.SMBus(1)
now = datetime.datetime.now()
print now.year
NowTime = map(lambda x:int(str(x),16),[now.second,now.minute,now.hour,now.weekday(),now.day,now.month,now.year%2000])
print NowTime
def ds3231SetTime():
    bus.write_i2c_block_data(address,register,NowTime)

def ds3231ReadTime():
    return bus.read_i2c_block_data(address,register,7)
    
    
ring = 0x20
def beep_up():
    bus.write_byte(ring,0x7F&bus.read_byte(ring))

def beep_off():
    bus.write_byte(ring,0x80|bus.read_byte(ring))
    
ds3231SetTime()
while True:
    
    t = ds3231ReadTime()
    print('%02x:%02x:%02x'% (t[2],t[1],t[0]))
    if t[0] == 0:
        beep_up()
    else:
        beep_off()
    time.sleep(1)