import video_to_img as vti
import img_to_video as itv

import sys



def main(argv):    
    
    print(argv)

    if(len(argv) < 2 or argv[1] == 'help' or  argv[1] == 'h' or argv[1] == '-help' or argv[1] =='-h'):
        print(''' 
-- MANUAL --
Usage:  'path to source vid' 'path to exit video' [-f__] 

    -f__ framrate of source video (output one will be the same)
                ''')
        return

    if(len(argv) < 3):        
        print("Not enough arguments")
        print("Usage:  'path to source vid' 'path to exit video' [-f__] ")



    

   

if __name__ == "__main__":
   main(sys.argv)