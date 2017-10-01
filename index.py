from pytube import YouTube
from moviepy.editor import VideoFileClip, concatenate_videoclips
path = '/home/jajoosam/Documents/Code/10k1/'

def merge(vid1yt, vid2path, vid3yt):
	# Video 1
	uno = YouTube(vid1yt)
	video = uno.get("mp4", "720p")
	video.download(path)
	uno = uno.filename + ".mp4"
	print (uno)

	# Video 2

	dos = vid2path
	print (dos)

	# Video 3

	tres = YouTube(vid3yt)
	video = tres.get("mp4", "720p")
	video.download(path)
	tres = tres.filename + ".mp4"
	print (tres)

	# Setting up moviePy files

	clip1 = VideoFileClip(uno)
	clip2 = VideoFileClip(dos)
	clip3 = VideoFileClip(tres)


	# Merging Videos
	final_clip = concatenate_videoclips([clip1,clip2,clip3])

	# Writing final file
	final_clip.write_videofile("final.webm")

	return "final.webm"