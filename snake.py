import SSD1306
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont
import spidev as SPI
import time, datetime
import random
import smbus
import threading
import 04_02 as oled

address = 0x20
bus = smbus.SMBus(1)
dirsel = {0:None, 1:'l',2:'u',3:'ul',4:'d',5:'ld',8:'r',10:'ru',12:'rd'}
print dirsel[1]

global input
input = 0

gamearea = [[0 for i in range(42)] for j in range(42)]

for i in range(42):
    gamearea[0][i] = gamearea[i][0] = gamearea[41][i] = gamearea[i][41] = 1

length = 10
head = [random.randint(5,35) for i in range(2)]

body = list()
direction = [-1,0]
body.append(head[:])
gamearea[head[0]][head[1]] = 1

target = [random.randint(5,35) for i in range(2)]
while target in body:
    target = [random.randint(5,35) for i in range(2)]
    
gamearea[target[0]][target[1]] = 1

get_direction():
    input = (~bus.read_byte(address)& 0xF)
    if not input == 0:
        direction = {'l':[-1,0],'r':[1,0],'d':[0,1],'u':[0,-1],'lu':[-1,-1],'ld':[-1,1],'ru'[1,-1],'rd':[1,1]}[input]

while True:
    threading.thread(target=get_direction)
    time.sleep(0.5)
    if length == 0:
        tail = body[-1]
        gamearea[body[0]][body[1]] = 0
        
    head[0] += direction[0]
    head[1] += direction[1]
    if not (head[0] in range(0,40) and head[1] in range(0,40)):
        break
    body.insert(0,head[:])
    gamearea[head[0]][head[1]] = 1
        
    




    