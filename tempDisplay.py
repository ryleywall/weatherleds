#--------------------------------------
#Authors: Ryley Wall & Austin Pelltier
#Wentworth Institute of Technolgy
#Networking Programming final project
#--------------------------------------
#The following code replicates initialization techniques used in the example code of the 
#raspberry pi neopixel python library & utilizes darksky API for weather information
#---------------------------------------------------------------------------------------------
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time

from neopixel import *
from darksky import forecast
from datetime import datetime as dt


# LED strip configuration:
LED_COUNT      = 40      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.SK6812_STRIP_RGBW	

#function to display a given color across all of the LEDS
def colorPut(strip , color):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i , color)
	strip.show()
	
def temp2Color(temp):
	maxTemp = 115.0
	minTemp = 15.0
	diff = maxTemp - minTemp
	section = diff / 2.0
	secNum = 0
	ratio = (temp - minTemp) / section
	if temp < tempMin:
		colorPut(strip , Color(0 , 0 , 255))
		return
	elif temp > tempMax:
		colorPut(strip , Color(255 , 0 , 0))
		return
	
	if ratio > 1:
		ratio = (temp - minTemp + section) / section
		secNum = secNum + 1
	
	if secNum == 0:
		colorPut(strip , Color(0 , 255.0*ratio , 255 - 255.0*ratio))
		return
	elif secNum == 1:
		colorPut(strip , Color( 255*ratio , 255 - 255.0*ratio , 0 ))
		return
	

#start of the main function
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()
	
	BOSTON = '646259b409b04e6f13d26b88a31e3ba2' , 42.3601, -71.0589
	
	with forecast(*BOSTON) as boston:	
		temperature = boston.temperature
		print 'The temperature is: ' , temperature
		displayColor = temp2Color(temperature)
		colorPut(displayColor)
