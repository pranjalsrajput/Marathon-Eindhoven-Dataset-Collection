import imageio
import numpy as np
import glob
import os

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


if __name__ == '__main__':
    #mergeGIFs('H','/home/pranjal/Documents/PythonProjects/Marathon-Eindhoven-Dataset-Collection/VideoAndImageGrid/GIFs/')
    mergeGIFs('V', '/home/pranjal/Documents/PythonProjects/Marathon-Eindhoven-Dataset-Collection/VideoAndImageGrid/HorizontalGIFs/')
