import imageio
import cv2
import imageio
import numpy as np
import glob
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import natsort
from pygifsicle import optimize

def trimVideo(input_video, start_time, end_time):
    output=input_video.split(".")[0]+"_trimmed.mp4"
    ffmpeg_extract_subclip(input_video, start_time, end_time, targetname=output)
    print("Start extracting frames")
    extractVideoFrames(output)
    print("End extracting frames")

#-----------------Start: Code to extract the video frames------------------------------#

def resizeImage(img):
    #print('Original Dimensions : ', img.shape)
    scale_percent = 20  # percent of original size
    # width = int(img.shape[1] * scale_percent / 100)
    # height = int(img.shape[0] * scale_percent / 100)
    dim = (256, 144)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    #print('Resized Dimensions : ', resized.shape)
    return resized

def extractVideoFrames(input_video):
    cap = cv2.VideoCapture(input_video)
    i = 0
    while (cap.isOpened()):
        #cap.set(cv2.CAP_PROP_POS_MSEC, (i * 1000))
        ret, frame = cap.read()
        #shape=frame.shape
        if ret == False:
            break
        frame=resizeImage(frame)
        #print("old size: "+str(shape)+", new size: " + str(frame.shape))
        #frame = cv2.medianBlur(frame, 9)  # blurring the image
        # cv2.imwrite(input_video.split(".")[0]+'_' + str(
        #         i) + '.jpg', frame,[cv2.IMWRITE_JPEG_QUALITY, 99])
        cv2.imwrite(input_video.split(".")[0] + '_' + str(
            i) + '.jpg', frame)
        i += 1

    cap.release()
    cv2.destroyAllWindows()
#-----------------End: Code to extract the video frames------------------------------#

#-----------------Start: Code to create the GIFs from frames------------------------------#
def createGIF(path_to_frames):

    files=[]
    for filename in glob.glob(os.path.join(path_to_frames, '*.jpg')):
        #print(filename)
        files.append(filename)
    files=natsort.natsorted(files)

    with imageio.get_writer(path_to_frames+'_GIF_.gif', mode='I', duration=(1/30)) as writer:
        #print("filenames")
        for file in files:
        # for filename in glob.glob(os.path.join(path_to_frames, '*.jpg')):
            #print(file)
            image = imageio.imread(file)
            writer.append_data(image)
        #print(files)
    #optimize(path_to_frames+'_GIF_blurred2.gif')
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
        gifPath='/home/pranjal/Documents/PythonProjects/Marathon-Eindhoven-Dataset-Collection/VideoAndImageGrid/HorizontalGIFs/output4.gif'
        output_gif = imageio.get_writer(gifPath, mode='I', duration=(1/30))
    if (mergeType == 'V'):
        gifPath='/home/pranjal/Documents/PythonProjects/Marathon-Eindhoven-Dataset-Collection/VideoAndImageGrid/VerticalGIFs/output.gif'
        output_gif = imageio.get_writer(gifPath, mode='I', duration=(1/30))

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
    #optimize(gifPath)

def make_GIF():
    textfilename = "./listOfVideos.txt"
    # counter=0
    with open(textfilename, 'r') as line:
        for videoInfo in line:
            videoInfo = videoInfo.rstrip('\n')
            # if(counter==0):
            if ('=' in videoInfo):
                pathToVideoFrames = videoInfo.split('=')[1]
                print("pathToVideoFrames: ", pathToVideoFrames)
            # counter+=1
            # else:
            if (',' in videoInfo):
                path = videoInfo.split(',')[0]
                print("videos: ", path)
                startSec = int(videoInfo.split(',')[1])
                endSec = int(videoInfo.split(',')[2])
                trimVideo(path, startSec, endSec)  # Trim an input video, giving start and end time(in sec)
    print("creating GIF")
    createGIF(pathToVideoFrames)

if __name__=="__main__":
    print("Start")
    mergeGIFs('H','/home/pranjal/Documents/PythonProjects/Marathon-Eindhoven-Dataset-Collection/VideoAndImageGrid/GIFs/')                 #Merge GIFs horizontally
    #mergeGIFs('V','/home/pranjal/Documents/PythonProjects/Marathon-Eindhoven-Dataset-Collection/VideoAndImageGrid/HorizontalGIFs/')        #Merge Horizontally merged GIFs vertically
    # for filename in glob.glob(os.path.join('/home/pranjal/Documents/Assignments/Deep Learning Project/NewDataset/Videos For Sample/36/trimmed/', '*.mp4')):
    #     extractVideoFrames(filename)                                                                                                       #Extract frames from a video
    #createGIF('/home/pranjal/Documents/Assignments/Deep Learning Project/NewDataset/Videos For Sample/2_/')
    #trimVideo("/home/pranjal/Documents/Assignments/Deep Learning Project/NewDataset/Videos For Sample/37/VID_20191013_113955746_6to9sec.mp4",6,9)

    #make_GIF()
    print("Done")
