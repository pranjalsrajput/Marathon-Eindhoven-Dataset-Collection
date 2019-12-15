import imageio
import cv2
import imageio
import numpy as np
import glob
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def trimVideo(input_video, start_time, end_time):
    ffmpeg_extract_subclip(input_video, start_time, end_time, targetname=input_video.split(".")[0]+"_trimmed.mp4")

#-----------------Start: Code to extract the video frames------------------------------#
def extractVideoFrames(input_video):
    cap = cv2.VideoCapture(input_video)
    i = 0
    while (cap.isOpened()):
        #cap.set(cv2.CAP_PROP_POS_MSEC, (i * 1000))
        ret, frame = cap.read()
        if ret == False:
            break
        cv2.imwrite(input_video.split(".")[0]+'_' + str(
                i) + '.jpg', frame)
        i += 1

    cap.release()
    cv2.destroyAllWindows()
#-----------------End: Code to extract the video frames------------------------------#

#-----------------Start: Code to create the GIFs from frames------------------------------#
def createGIF(path_to_frames):
    filenames = [
        path_to_frames+'VID_20191013_110221359_trimmed_0.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_1.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_2.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_3.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_4.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_5.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_6.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_7.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_8.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_9.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_10.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_11.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_12.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_13.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_14.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_15.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_16.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_17.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_18.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_19.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_20.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_21.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_22.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_23.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_24.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_25.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_26.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_27.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_28.jpg',
        path_to_frames+'VID_20191013_110221359_trimmed_29.jpg',]

    with imageio.get_writer(path_to_frames+'_GIF2.gif', mode='I') as writer:
        for filename in filenames:
        # for filename in glob.glob(os.path.join(path_to_frames, '*.jpg')):
            image = imageio.imread(filename)
            writer.append_data(image)
# -----------------End: Code to create the GIFs from frames------------------------------#

def mergeGIFs(mergeType,path):
    gifList=[]
    gifLength_List = []

    for filename in glob.glob(os.path.join(path, '*.gif')):
        inputGif=imageio.get_reader(filename)
        gifList.append(inputGif)
        gifLength_List.append(inputGif.get_length())

    # If they don't have the same number of frame take the shorter
    number_of_frames = min(gifLength_List)

    # Create writer object
    # new_gif = imageio.get_writer('output.gif')
    if(mergeType=='H'):
        output_gif = imageio.get_writer('/home/pranjal/Documents/PythonProjects/Marathon-Eindhoven-Dataset-Collection/VideoAndImageGrid/HorizontalGIFs/output4.gif')
    if (mergeType == 'V'):
        output_gif = imageio.get_writer('/home/pranjal/Documents/PythonProjects/Marathon-Eindhoven-Dataset-Collection/VideoAndImageGrid/HorizontalGIFs/output.gif')

    # output_gif = imageio.get_writer('/home/pranjal/Documents/PythonProjects/Marathon-Eindhoven-Dataset-Collection/VideoAndImageGrid/HorizontalGIFs/output4.gif')
    output_gif = imageio.get_writer(
        '/home/pranjal/Documents/PythonProjects/Marathon-Eindhoven-Dataset-Collection/VideoAndImageGrid/VerticalGIFs/output4.gif')

    for frame_number in range(number_of_frames):
        gifFrameList=[]
        for gif in gifList:
            gifFrameList.append(gif.get_next_data())

        # here is the magicVerticalGIFs
        if(mergeType=='H'):
            new_image = np.hstack((gifFrameList))
        if (mergeType == 'V'):
            new_image = np.vstack((gifFrameList))

        output_gif.append_data(new_image)

    for gif in gifList:
        gif.close()
    output_gif.close()


if __name__=="__main__":
    print("Start")
    # mergeGIFs('H','/home/pranjal/Documents/PythonProjects/Marathon-Eindhoven-Dataset-Collection/VideoAndImageGrid/GIFs/')                 #Merge GIFs horizontally
    #mergeGIFs('V','/home/pranjal/Documents/PythonProjects/Marathon-Eindhoven-Dataset-Collection/VideoAndImageGrid/HorizontalGIFs/')        #Merge Horizontally merged GIFs vertically
    #extractVideoFrames('/home/pranjal/Documents/Assignments/Deep Learning Project/NewDataset/Videos For Sample/35/VID_20191013_135859615_trimmed.mp4')                                                                                                                   #Extract frames from a video
    createGIF('/home/pranjal/Documents/Assignments/Deep Learning Project/NewDataset/Videos For Sample/35/Frames/')
    #trimVideo('/home/pranjal/Documents/Assignments/Deep Learning Project/NewDataset/Videos For Sample/35/VID_20191013_135859615.mp4',60,62) #Trim an input video, giving start and end time(in sec)
    print("Done")
