#!/usr/local/bin/python3
import pandas as pd

# import pickle
import dill as pickle
from PIL import Image
from moviepy.editor import *
from matplotlib import cm
import numpy as np

def my_map(x,in_min,in_max,out_min,out_max):
	'''! Standard mapping formula. Used in many places'''
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def convert_coords_dms_to_decimal(in_txt):
	# Decimal Degrees = degrees + (minutes/60) + (seconds/3600)

	try:
		degrees=str(in_txt).split('.')[0]
		minutes=int(degrees[2:])

		degrees=int(degrees[:2])

		seconds=int(str(in_txt).split('.')[1])/100


		out=degrees+(minutes/60) + (seconds/3600)
	except Exception as e:
		out="XX"

	# print (degrees,minutes,seconds,"-->",out)

	return out

def pickle_data(out_list,fil):
	print (f"Saving data to {fil}")
	with open(fil, 'wb') as f:
		pickle.dump(out_list, f)

def unpickle_data(fil):
	# Pickle read
	print (f"\nReading from {fil}")
	with open(fil, 'rb') as f:
		mynewlist = pickle.load(f)
	return mynewlist

# From gpsvisualizer:
# center: 37.74433,-89.12340
# SW corner: 37.65100,-89.34219
# NE corner: 37.83767,-88.90461


# lat/long limits for world map
left_lim=-89.34219
right_lim=-88.90461
top_lim=37.83767
bottom_lim=37.65100


# WORLD_MAP: 530 by 266
PIC_W=700
PIC_H=377

# ---------------------------
# Coords in DMS:
curr_lat=3743.9362
curr_long=8911.4735
curr_heading=170
# ---------------------------


curr_lat=convert_coords_dms_to_decimal(curr_lat)
curr_long=-1*convert_coords_dms_to_decimal(curr_long)


print (f"LAT,LONG: {curr_lat},{curr_long}")
print (f"Heading: {curr_heading}")


y=int(round(my_map(curr_lat,top_lim,bottom_lim,0,PIC_H),0))
x=int(round(my_map(curr_long,left_lim,right_lim,0,PIC_W),0))

print (f"Co-ords on image: {x},{y}")



# ================================================================

# Opening the primary image (used in background)
img1 = Image.open(r"track-simple.png")

# Opening the secondary image (overlay image)
img2 = Image.open(r"marker.png")

# rotating a image 90 deg counter clockwise
img2 = img2.rotate(360-curr_heading, Image.NEAREST, expand = 1)


# Pasting img2 image on top of img1
# starting at coordinates (0, 0)
img1.paste(img2, (x,y), mask = img2)

# # # Displaying the image
# # img1.show()

# save a image using extension
im_name=f"rendered_imgs/track_({x},{y})_{curr_heading}deg.png"
img1 = img1.save(im_name)

# ================================================================
finalList=[]

i=im_name

curr_map = ImageClip(i, duration=2400)
curr_map = curr_map.set_start(29)
curr_map = curr_map.set_position((1920-PIC_W-5, 1080-PIC_H-30))
finalList.append(curr_map)

# print (finalList)

pickle_data(finalList,"../tracks.pkl")
print(unpickle_data("../tracks.pkl"))
# --------------------------------------------------------------
