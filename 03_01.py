import time

device_folder = '/sys/bus/w1/devices/28-0000096508a9'
device_file = device_folder + '/w1_slave'

def read_rom():
    name_file = device_folder + '/name'
    with open(name_file, 'r') as f:
        return f.readline()

def read_temp_raw():
    with open(device_file, 'r') as f:
        return f.readlines()

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

def main():
    print(' rom: ' + read_rom())
    while True:
        print(' C=%3.3f F=%3.3f' % read_temp())
        time.sleep(1)

if __name__ == '__main__':
    main()