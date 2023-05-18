import cv2
import os


def img_to_vid( video_name):
    print("img_to_vid_ffmpeg starting...")

    # we will use this short name to name our outout video 
    short_video_name = str(video_name).split("\\")
    short_video_name = short_video_name[len(short_video_name) -1]
    print("Short name: " + short_video_name)

    #image_folder = 'images'
    image_folder = 'C:\Fajlovi\Projekti\Ivans Video Upscaleer IVU\Ivan\'s video upscaler\images'
    video_name =  str(short_video_name) + '_UPSCALED.avi'

    #images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    try:
        frame = cv2.imread(os.path.join(image_folder, images[0]))
        height, width, layers = frame.shape
    
    except Exception as e: print(e)

    #video = cv2.VideoWriter(video_name, 0, 1, (width,height))
    video = cv2.VideoWriter(video_name, 0, 30, (width,height))

    sorted(images)
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    print("img_to_vid ending...")
    cv2.destroyAllWindows()
    video.release()