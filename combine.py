#!/usr/local/bin/python3

# Import everything needed to edit video clips
from moviepy.editor import *
import os

# from moviepy.video.fx import volumex, resize, mirrorx
# >>> clip.fx( volumex, 0.5).fx( resize, 0.3).fx( mirrorx )

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
FPS=5

vid_concat_list=[]

total_time=0
for vid_name in vid_list[-3:-1]:
	clip=VideoFileClip(in_dir+vid_name).without_audio()
	print (clip.fps)
	exit()
	clip = clip.set_fps(FPS)

	t=clip.duration
	print (f"{vid_name} duration: {t}s")
	total_time+=t

	vid_concat_list.append(clip)

print (f"\ntotal_time: {total_time}")

# ---------------------------------------------------------------- #

raw_vids_combined = concatenate_videoclips(vid_concat_list)

print (f"\ntotal_time: {raw_vids_combined.duration}")


sat_icon = ImageClip('satellite.png', duration=total_time)
sat_icon = sat_icon.set_position((100, 950))
finalList=[raw_vids_combined,sat_icon]




final_video = CompositeVideoClip(finalList)




#writing the video into a file / saving the combined video
final_video.write_videofile("merged_&_composited.mp4",threads = 4,  audio=False,remove_temp=True)
 
# # showing final clip
# final.ipython_display(width = 480)