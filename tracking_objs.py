from moviepy.editor import VideoFileClip
from moviepy.video.tools.tracking import manual_tracking
clip = VideoFileClip("myvideo.mp4")
# manually indicate 3 trajectories, save them to a file
trajectories = manual_tracking(clip, t1=5, t2=7, fps=5,
                                   nobjects=3, savefile="track.txt")
# ...
# LATER, IN ANOTHER SCRIPT, RECOVER THESE TRAJECTORIES
from moviepy.video.tools.tracking import Trajectory
traj1, traj2, traj3 = Trajectory.load_list('track.txt')
 # If ever you only have one object being tracked, recover it with
traj, =  Trajectory.load_list('track.txt')