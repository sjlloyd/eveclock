import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Image
import ImageDraw
import ImageFont
from datetime import datetime
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
fontPath = "/usr/share/fonts/truetype/droid/DroidSansMono.ttf"
sans16 = ImageFont.truetype ( fontPath, 16 )


while True:
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	currentTime = datetime.now().strftime("Local: %H:%M")
	eveTimeString = datetime.utcnow().strftime("EVE  : %H:%M")

	draw.text((0,0), currentTime, font=sans16, fill=255)
	draw.text((0,17), eveTimeString, font=sans16, fill=255)

	disp.image(image)
	disp.display()
	time.sleep(1)
