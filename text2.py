#!/usr/local/bin/python3


# ========================================================================
# ========================================================================
# STAGE 2
# ========================================================================
# ========================================================================
from moviepy.editor import *
import os
# ---------------------------------------------------------------- #
def get_vids(in_dir):
	vid_list=[]
	for (root,dirs,files) in os.walk(in_dir, topdown=True):
		# print (root)
		# print (dirs)
		for f in sorted(files):
			if f.split(".")[1]=="mp4":
				vid_list.append(f)
	print(f"\n#vids found: {len(vid_list)}\n")
	return vid_list

# ---------------------------------------------------------------- #
# Load vids
in_dir="front/"
vid_list=get_vids(in_dir)
# FPS=30.0052
FPS=1

vid_concat_list=[]

total_time=0
total_frames=0
for vid_name in vid_list:
	clip=VideoFileClip(in_dir+vid_name).without_audio()
	clip = clip.set_fps(FPS)
	FPS=clip.fps
	t=clip.duration
	f=clip.reader.nframes

	# print (f"\n{vid_name}")
	print (f"{vid_name} --> t: {t}s, FPS:{FPS}, #frames:{f}")


	total_time+=t
	total_frames+=f

	vid_concat_list.append(clip)

print (f"\nINPUT:\n---> total_time: {total_time}s, total_frames: {total_frames}")

# ---------------------------------------------------------------- #

raw_vids_combined = concatenate_videoclips(vid_concat_list)


print ("\nOUTPUT:")
print (f"---> total_time: {raw_vids_combined.duration}s, total_frames: {raw_vids_combined.fps*raw_vids_combined.duration}")
# n_frames = raw_vids_combined.nframes
print (f"FPS: {raw_vids_combined.fps}\n")


finalList=[]

sat_icon = ImageClip('satellite.png', duration=total_time)
sat_icon = sat_icon.set_position((100, 950))
finalList+=[raw_vids_combined,sat_icon]

# ========================================================================
# ========================================================================
# STAGE 3
# ========================================================================
# ========================================================================
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

import pandas as pd

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

# =======================================================
# Load data
# df=pd.read_excel("front/gps_data.xlsx",sheet_name="Summary")
df=pd.read_excel("gps.xlsx")
speeds=list(df["Speed (MPH)"])
headings=list(df["Heading"])
satellites=fix_sats(list(df["#SVs"].fillna(0)))


total_len=len(speeds)
print (f"len:{total_len}")

starts=[i for i in range(0,total_len)]
durations=[1 for i in range(0,total_len)]

# # print (starts)
# # print (durations)
# print (satellites)
# print (speeds)
# print (headings)
# exit()



# ========================================================================
def render_speed(speeds, starts, durations):
	outlist=[]
	i=1
	for text,t,duration in zip(speeds, starts, durations):
		txt_clip = TextClip(str(text)+"MPH",fontsize = SPEED_TXT_SIZE, color=SPEED_TXT_COLOR)
		txt_clip = txt_clip.set_start(t)
		# txt_clip = txt_clip.set_pos('center').set_duration(duration)
		txt_clip = txt_clip.set_pos(SPEED_TXT_POS).set_duration(duration)
		outlist.append(txt_clip)
		print (f"render speed {i} of {total_len}")
		i+=1
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
	i=1
	for text,t,duration in zip(headings, starts, durations):
		txt_clip = TextClip(str(text)+HEADING_SUFFIX,fontsize = HEADING_TXT_SIZE, color=HEADING_TXT_COLOR)
		txt_clip = txt_clip.set_start(t)
		# txt_clip = txt_clip.set_pos('center').set_duration(duration)
		txt_clip = txt_clip.set_pos(HEADING_TXT_POS).set_duration(duration)
		headings_list.append(txt_clip)
		print (f"render headings {i} of {total_len}")
		i+=1
	return headings_list

# print ("rendering speed...")
# finalList+=render_speed(speeds, starts, durations)

# with open(SPEEDS_FILE, 'wb') as f:
# 		pickle.dump(render_speed(speeds, starts, durations), f)

# print ("rendering sats...")
# finalList+=render_sats(satellites, starts, durations)

# print ("rendering headings...")
# finalList+=render_headings(headings, starts, durations)

import dill as pickle
def unpickle(fil):
	# Pickle read
	print (f"\nReading from {fil}")
	with open(fil, 'rb') as f:
		mynewlist = pickle.load(f)
	return mynewlist

print ("rendering speed...")
finalList+=unpickle(SPEEDS_FILE)
print ("rendering sats...")
finalList+=unpickle(SATS_FILE)
print ("rendering headings...")
finalList+=unpickle(HEADINGS_FILE)


print ("rendering tracks...")
finalList+=unpickle("tracks.pkl")


final_video = CompositeVideoClip(finalList)

final_video.write_videofile(f"merged_&_composited_{FPS}fps.mp4",
	threads = 10,
	audio=False,)
	# remove_temp=True,
	# codec="mpeg4")


# Some examples of codecs are:
# 'libx264' (default codec for file extension .mp4) makes well-compressed videos (quality tunable using ‘bitrate’).
# 'mpeg4' (other codec for extension .mp4) can be an alternative to 'libx264', and produces higher quality videos by default.
# 'rawvideo' (use file extension .avi) will produce a video of perfect quality, of possibly very huge size.
# png (use file extension .avi) will produce a video of perfect quality, of smaller size than with rawvideo.
# 'libvorbis' (use file extension .ogv) is a nice video format, which is completely free/ open source. However not everyone has the codecs installed by default on their machine.
# 'libvpx' (use file extension .webm) is tiny a video format well indicated for web videos (with HTML5). Open source.