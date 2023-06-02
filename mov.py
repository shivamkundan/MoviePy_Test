#!/usr/local/bin/python3

import numpy as np
from moviepy.editor import *

#ffmpeg -y -f lavfi -i color=black:size=720x1280:rate=10:duration=10 -vcodec libx264 original_video.mp4
#ffmpeg -y -f lavfi -i testsrc=size=720x1280:rate=1:duration=1 -frames 1 -update 1 watermark.png

finalList = []
first = 4

backTemp = VideoFileClip("small.mp4").without_audio()
(w, h) = backTemp.size

print (f"backTemp.size: {backTemp.size}")

for item in dir(backTemp):
	print (item)
print()


back = backTemp  # The example assumes that backTemp resolution is 720x1280, and duration is 10 seconds
finalList.append(back)

image = ImageClip('satellite.png', duration=5)
most_left_col = -image.size[0]
end_t = np.log(-most_left_col)/5 + first

image = image.set_position(lambda t: ((np.exp(10*(t - first))*(-1) if t < end_t else most_left_col - np.exp(10*(t-end_t))*(-1)), 100))
image.fps = 10  # Set to 10 fps for testing\
finalList.append(image)

print (finalList)

# videoTemp = CompositeVideoClip(finalList)
# videoTemp.write_videofile("TEST_FinalVideoTT" + ".mp4")