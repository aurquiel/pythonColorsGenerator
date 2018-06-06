#!/usr/bin/python3.5

import cv2
import os
import random

#Getting hex code of red colors
hexCodeList = []

for i in range(0, 16777215, 100): 					#from 0 to FFFFFF with 100K as interval
	hexCode = hex(i).strip("0x") 					#strip 0x
	if len(hexCode) < 6:     						#fill the gaps with "0"
		for j in range(len(hexCode), 6):
			hexCode += "0"
	hexCodeList.append(hexCode) 					#add to list

print("Done1")
#Getting RGB tuples
rgbCodeList = []

for elements in hexCodeList:
	rgbCodeList.append(tuple(int(elements[i:i+2], 16) for i in (0, 2 ,4))) #save the RGB as tuples

print("Done2")
#Rgb to HVS
import colorsys

hvsCodeList = []

for elements in rgbCodeList:
	hvsCodeList.append(colorsys.rgb_to_hsv( int(elements[0]), int(elements[1]), int(elements[2]) ))

print("Done3")
#Get the colors separationhvs

rgbListRed = []
rgbListYellow = []
rgbListGreen = []
rgbListBlueLight = []
rgbListBlue = []
rgbListPurple = []

for elements in hvsCodeList:
	if float(elements[0])*360 <= 30 or float(elements[0])*360 > 330:
		rgbListRed.append(colorsys.hsv_to_rgb(float(elements[0]), float(elements[1]), float(elements[2])))
	elif float(elements[0])*360 <= 90 and float(elements[0])*360 > 30:
		rgbListYellow.append(colorsys.hsv_to_rgb(float(elements[0]), float(elements[1]), float(elements[2])))
	elif float(elements[0])*360 <= 150 and float(elements[0])*360 > 90:
		rgbListGreen.append(colorsys.hsv_to_rgb(float(elements[0]), float(elements[1]), float(elements[2])))
	elif float(elements[0])*360 <= 210 and float(elements[0])*360 > 150:
		rgbListBlueLight.append(colorsys.hsv_to_rgb(float(elements[0]), float(elements[1]), float(elements[2])))
	elif float(elements[0])*360 <= 270 and float(elements[0])*360 > 210:
		rgbListBlue.append(colorsys.hsv_to_rgb(float(elements[0]), float(elements[1]), float(elements[2])))
	elif float(elements[0])*360 <= 330 and float(elements[0])*360 > 270:
		rgbListPurple.append(colorsys.hsv_to_rgb(float(elements[0]), float(elements[1]), float(elements[2])))

#Create images

import numpy as np

def createBlank(width, height, rgb_color=(0, 0, 0)):
	""""Create new image(numpy array) filled with certain color in RGB"""
	image = np.zeros((height, width, 3), np.uint8)

    	#Since OpenCV uses BGR, convert the color first
	color = tuple(reversed(rgb_color))

	# Fill image with color
	image[:] = color

	return image

# Create new 10x10 image
width, height = 40, 66

path = os.getcwd()+"/colors/"

iterator = 1
for elements in rgbListRed:
	image = createBlank(width, height, elements)
	name = path + "red" + str(iterator) + ".jpg"
	cv2.imwrite(name, image)
	iterator += 1

iterator = 1
for elements in rgbListYellow:
	image = createBlank(width, height, elements)
	name = path+"yellow" + str(iterator) + ".jpg"
	cv2.imwrite(name, image)
	iterator += 1

iterator = 1
for elements in rgbListGreen:
	image = createBlank(width, height, elements)
	name = path + "green" + str(iterator) + ".jpg"
	cv2.imwrite(name, image)
	iterator += 1

iterator = 1
for elements in rgbListBlueLight:
	image = createBlank(width, height, elements)
	name = path + "blueLigth" + str(iterator) + ".jpg"
	cv2.imwrite(name, image)
	iterator += 1

iterator = 1
for elements in rgbListBlue:
	image = createBlank(width, height, elements)
	name = path + "blue" + str(iterator) + ".jpg"
	cv2.imwrite(name, image)
	iterator += 1

iterator = 1
for elements in rgbListPurple:
	image = createBlank(width, height, elements)
	name = path + "purple" + str(iterator) + ".jpg"
	cv2.imwrite(name, image)
	iterator += 1

#transform them to Garyscale
pathGray = os.getcwd()+"/gray/"
"""
iterator = 1
for root, dirs, files in os.walk(os.path.abspath(path)):
	for file in files:
		image = cv2.imread(os.path.join(root, file), 0)
		name = pathGray+"gray"+str(iterator)+".jpg"
		cv2.imwrite(name, image)
		iterator += 1
"""
files=[]

for fileName in os.listdir(path):
	files.append(fileName)

iterator=1
random.shuffle(files)

for item in files:
  image = cv2.imread(os.path.join(path,item), 0)
  name = pathGray+"gray"+str(iterator)+".jpg"
  cv2.imwrite(name, image)
  iterator += 1
