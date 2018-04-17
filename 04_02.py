import SSD1306
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont
import spidev as SPI
import time, datetime

RST = 19
DC = 16
bus = 0
device = 0
disp = SSD1306.SSD1306(rst=RST,dc=DC,spi=SPI.SpiDev(bus,device))

disp.begin()
disp.clear()
disp.display()

if name == '__main__':
    while True:
        font = ImageFont.load_default()
        logo = Image.open('pic.png').convert("1")
        blank = Image.new("1",[128,64])
        draw = ImageDraw.Draw(blank)
        draw.bitmap((0,0),logo,fill=1)
        draw.text((80,0),datetime.datetime.now().strftime('%H:%M:%S'),font=None,fill=255)
        second = (datetime.datetime(2018,5,4)-datetime.datetime.now()).total_seconds()
        draw.text((80,30),"%d days \r\n%02d:%02d:%02d"%(second/86400,(second%86400)//3600,(second%3600)/60,second%60),font=font,fill=255)
        disp.image(blank)
        disp.display()
