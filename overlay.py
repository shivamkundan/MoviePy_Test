#!/usr/local/bin/python3

# Crop a rectangle centered in x,y=(300,400), width=50, height=150 :

# crop(clip,  x_center=300 , y_center=400,
#                     width=50, height=150)

# myClip.resize( (460,720) ) # New resolution: (460,720)
# myClip.resize(0.6) # width and height multiplied by 0.6
# myClip.resize(width=800) # height computed automatically.


from moviepy.editor import VideoFileClip, CompositeVideoClip
zm_video_path = "1.mov"


def add_zm(fg_in_bg_avi):
    clip1 = VideoFileClip(fg_in_bg_avi)
    clip3 = VideoFileClip(zm_video_path, has_mask=True)
    video = CompositeVideoClip([clip1, clip3])
    name = 'New_video'
    video.write_videofile(name, audio=False)  # No audio first
    video.close()
    return name


if __name__ == '__main__':
    video_have_zm = add_zm("background.mp4")


# =================================================================



output_path="output.mp4"

video_clip = VideoFileClip((video_view), target_resolution=(1080, 1920)) #b .mp4 file

overlay_clip = VideoFileClip((animeeer), has_mask=True, target_resolution=(1080, 1920)) #.mov file with alpha channel


final_video = mp.CompositeVideoClip([video_clip, overlay_clip])  


final_video.write_videofile(
    output_path,
    fps=30,
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
    threads = 6,
)