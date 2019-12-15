import imageio
import cv2
import imageio
import numpy as np
import glob
import os

#-----------------Start: Code to extract the video frames------------------------------#
def extractVideoFrames():
    cap = cv2.VideoCapture(
        '/home/pranjal/Documents/Assignments/Deep Learning Project/NewDataset/VID_20191013_120109.mp4')
    i = 0
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        cv2.imwrite(
            '/home/pranjal/Documents/PythonProjects/Marathon-Eindhoven-Dataset-Collection/VideoAndImageGrid/frames/VID_20191013_120109_' + str(
                i) + '.jpg', frame)
        i += 1

    cap.release()
    cv2.destroyAllWindows()
#-----------------End: Code to extract the video frames------------------------------#

#-----------------Start: Code to create the GIFs from frames------------------------------#
def createGIF():
    filenames = [
        '/home/pranjal/Documents/PythonProjects/Marathon-Eindhoven-Dataset-Collection/VideoAndImageGrid/frames/VID_20191013_120109_0.jpg',
        '/home/pranjal/Documents/PythonProjects/Marathon-Eindhoven-Dataset-Collection/VideoAndImageGrid/frames/VID_20191013_120109_100.jpg',
        '/home/pranjal/Documents/PythonProjects/Marathon-Eindhoven-Dataset-Collection/VideoAndImageGrid/frames/VID_20191013_120109_120.jpg',
        '/home/pranjal/Documents/PythonProjects/Marathon-Eindhoven-Dataset-Collection/VideoAndImageGrid/frames/VID_20191013_120109_127.jpg']

    with imageio.get_writer(
            '/home/pranjal/Documents/PythonProjects/Marathon-Eindhoven-Dataset-Collection/VideoAndImageGrid/GIFs/movie1.gif',
            mode='I', duration=0.5) as writer:
        for filename in filenames:
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
    # mergeGIFs('H','/home/pranjal/Documents/PythonProjects/Marathon-Eindhoven-Dataset-Collection/VideoAndImageGrid/GIFs/')
    mergeGIFs('V','/home/pranjal/Documents/PythonProjects/Marathon-Eindhoven-Dataset-Collection/VideoAndImageGrid/HorizontalGIFs/')
