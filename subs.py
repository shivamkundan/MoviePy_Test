#!/usr/local/bin/python3


# https://zulko.github.io/blog/2014/02/12/transcribing-piano-rolls/



from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

generator = lambda txt: TextClip(txt, font='Arial', fontsize=36, color='red')
subs = SubtitlesClip('subtitles.srt', generator)
subtitles = SubtitlesClip(subs, generator)

# txt_clip1 = txt_clip1.set_position((5,35))

video = VideoFileClip("small.mp4")
result = CompositeVideoClip([video, subtitles.set_pos(('center','bottom'))])

result.write_videofile("output.mp4")


# subtitles.srt:
