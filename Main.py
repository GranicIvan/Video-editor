import video_to_img as vti
import img_to_video as itv

print("Welcome to Ivan's video upscaler \n")

video_name = input()
vti.vid_to_img(video_name)

print("sada pravimo video...")


itv.img_to_vid(video_name)



print("Good bye!")