import cv2
import os


#Here we extract frames from video, adn store them in folder

def vid_to_img(video_name):
    print("vid_to_img strating...")
    print("Ime video fajla je: \'" + video_name + "\'" )

    #importing video
    cam = cv2.VideoCapture(video_name)
    currentframe = 0

    while(True):
        ret,frame = cam.read()
        if ret:
            #name = 'Video to Images\Frame(' + str(currentframe) + ').jpg'
            name = str(currentframe) + '.jpg'
            print("name: " + name)
            #cv2.imwrite(name, frame)
            path = 'C:\Fajlovi\Projekti\Ivans Video Upscaleer IVU\Ivan\'s video upscaler\images'
            cv2.imwrite(os.path.join(path , name), frame)
            currentframe += 1
            #print("processing frame num: " , str(currentframe))
        else:
            break

    cam.release()
    cv2.destroyAllWindows()