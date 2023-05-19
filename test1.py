import os

#os.system("ffmpeg -i a_UPSCALED.avi -b:v 4M movie.mp4")
os.system("ffmpeg -r 1 -i img%01d.png -vcodec mpeg4 -y movie.mp4")