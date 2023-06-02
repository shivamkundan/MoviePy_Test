#!/usr/local/bin/python3
import pandas as pd

# import pickle
import dill as pickle

from moviepy.editor import *

SPEED_TXT_POS=(400,980)
SPEED_TXT_SIZE=50
SPEED_TXT_COLOR="green"
SPEEDS_FILE="front/speeds_list.pkl"

SATS_TXT_POS=(100,980)
SATS_TXT_SIZE=50
SATS_TXT_COLOR="yellow"
SATS_FILE="front/sats_list.pkl"

HEADING_TXT_POS=(700,980)
HEADING_TXT_SIZE=50
HEADING_TXT_COLOR="red"
HEADING_SUFFIX="°"
HEADINGS_FILE="front/headings_list.pkl"

# =======================================================
# =======================================================

def fix_sats(sats_raw):
	prev_num_sats=-1

	# Substitute intermediate missing vals
	for i in range(0,len(sats_raw)):
		if sats_raw[i]==0:
			sats_raw[i]=prev_num_sats
		else:
			prev_num_sats=sats_raw[i]

	# Substitute initial missing vals
	for i in range(0,len(sats_raw)):
		if sats_raw[i]==-1:
			sats_raw[i]=0

	return sats_raw

def pickle_and_verify(out_list,fil):
	print (f"Saving speeds_list to {fil}")
	with open(fil, 'wb') as f:
		pickle.dump(out_list, f)

	# Pickle read
	print (f"\nReading from {fil}")
	with open(fil, 'rb') as f:
		mynewlist = pickle.load(f)

	print (f"#items [mynewlist]: {len(mynewlist)}")

	print ()


def unpickle(fil):
	# Pickle read
	print (f"\nReading from {fil}")
	with open(fil, 'rb') as f:
		mynewlist = pickle.load(f)
	return mynewlist
	# print (f"#items [mynewlist]: {len(mynewlist)}")

	# print ()

# =======================================================
# =======================================================

# Load data
df=pd.read_excel("gps.xlsx")
speeds=list(df["Speed (MPH)"])
headings=list(df["Heading"])
satellites=fix_sats(list(df["#SVs"].fillna(0)))


total_len=len(speeds)
print (f"len:{total_len}")

starts=[i for i in range(0,total_len)]
durations=[1 for i in range(0,total_len)]


def render_speed(speeds, starts, durations):
	outlist=[]
	i=1
	print("")
	for text,t,duration in zip(speeds, starts, durations):
		txt_clip = TextClip(str(text)+"MPH",fontsize = SPEED_TXT_SIZE, color=SPEED_TXT_COLOR)
		txt_clip = txt_clip.set_start(t)
		txt_clip = txt_clip.set_pos(SPEED_TXT_POS).set_duration(duration)
		outlist.append(txt_clip)
		print (f"render speed {i} of {total_len}")
		i+=1
	print ("")
	return outlist

def render_sats(satellites, starts, durations):
	sats=[]
	i=1
	for text,t,duration in zip(satellites, starts, durations):
		text=str(text).split(".")[0]
		txt_clip = TextClip(text,fontsize = SATS_TXT_SIZE, color=SATS_TXT_COLOR)
		txt_clip = txt_clip.set_start(t)
		# txt_clip = txt_clip.set_pos('center').set_duration(duration)
		txt_clip = txt_clip.set_pos(SATS_TXT_POS).set_duration(duration)
		sats.append(txt_clip)
		print (f"render sats {i} of {total_len}")
		i+=1
	return sats

def render_headings(headings, starts, durations):
	headings_list=[]
	i=0
	for text,t,duration in zip(headings, starts, durations):
		txt_clip = TextClip(str(text)+HEADING_SUFFIX,fontsize = HEADING_TXT_SIZE, color=HEADING_TXT_COLOR)
		txt_clip = txt_clip.set_start(t)
		# txt_clip = txt_clip.set_pos('center').set_duration(duration)
		txt_clip = txt_clip.set_pos(HEADING_TXT_POS).set_duration(duration)
		headings_list.append(txt_clip)
		print (f"render headings {i} of {total_len}")
		i+=1
	return headings_list

# =======================================================
# =======================================================

# # ----- render speed ----- #
# print ("rendering speed...")
# speeds_list=render_speed(speeds, starts, durations)
# print (f"\n#items [speeds_list]: {len(speeds_list)}")
# pickle_and_verify(speeds_list,SPEEDS_FILE)


# # ----- render sats ----- #
# print ("rendering sats...")
# sats_list=render_sats(satellites, starts, durations)
# print (f"\n#items [sats_list]: {len(sats_list)}")
# pickle_and_verify(sats_list,SATS_FILE)

# # ----- render headings ----- #
# print ("rendering headings...")
# headings_list=render_headings(headings, starts, durations)
# print (f"\n#items [headings_list]: {len(headings_list)}")
# pickle_and_verify(headings_list,HEADINGS_FILE)

# headings_list=unpickle(HEADINGS_FILE)

sats_list=unpickle(SATS_FILE)

print (len(sats_list))