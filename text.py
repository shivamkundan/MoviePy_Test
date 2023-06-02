#!/usr/local/bin/python3

import pandas as pd

df=pd.read_csv("speed.csv")

texts=list(df["Speed"])
starts=list(df["Start"])
durations=list(df["Duration"])




from moviepy.editor import *
import numpy as np
# picture = VideoFileClip("satellite.png", audio=False).set_duration(50)
# picture=VideoFileClip("front/20230528_190106_NF.mp4")
picture=VideoFileClip("small.mp4")

# textOne = "First Line!"
# textTwo = "Second Caption!!!!"
# textThree = "Third one!!!"

# texts = [textOne, textTwo, textThree]

# step = 15 #each 15 sec: 0, 15, 30
# duration = 10
# t = 0
# txt_clips = []
# for text,i in zip(texts,range(0,3)):
#   txt_clip = TextClip(text,fontsize = 40, color='red')
#   txt_clip = txt_clip.set_start(t)
#   # txt_clip = txt_clip.set_pos('center').set_duration(duration)
#   txt_clip = txt_clip.set_position((5,35)).set_duration(duration)
#   txt_clips.append(txt_clip)
#   t += step

# audio = AudioFileClip(r"C:\Users\Public\Music\Sample Music\Kalimba.mp3").subclip(0,50)
# video_with_new_audio = picture.set_audio(audio)

image = ImageClip('satellite.png', duration=5)
image = image.set_position((100, 100))
# image.fps = 10  # Set to 10 fps for testing\




# ======================================================================================
# For more flexibility, you can use not range(0,3) etc., but lists with the time points and durations, like with the captions; something like that:


finalList=[picture,image]
for text,t,duration in zip(texts, starts, durations):
    txt_clip = TextClip(text,fontsize = 40, color='red')
    txt_clip = txt_clip.set_start(t)
    txt_clip = txt_clip.set_pos('center').set_duration(duration)
    finalList.append(txt_clip)


print (finalList)

exit()

# txt_clips=picture+txt_clips+image
final_video = CompositeVideoClip(finalList)
final_video.write_videofile("TEXT.mp4")