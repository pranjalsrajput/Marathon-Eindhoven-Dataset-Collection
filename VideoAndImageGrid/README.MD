# Creating a Grid of GIFs

Few things need to take care of:

1. All the GIFs to be merged should be of same durations (containing the same number of frames)

2. For example, to create a GIF of 10sec duration, you should extract total 300 frames from the videos (if 2 videos, then extract 150 frames from each video). I have considered a frame rate of 30fps while creating the GIF. This value can be edited in the code.

## Ways to create a GIF

There are two ways to do this:

### A. Directly creating GIF from the video

1. Create a text file `listOfVideos.txt`. You can find attached an example file.

2. Mention the path of the folder containing the videos in the `path=` variable.

3. Also, mention the path of each video along with the start and end time (in seconds) of the video to be trimmed.

4. Save the file and run `makeGIF()` of `createGif.py`

5. This will firstly trim the videos according to the duration mentioned, then extract all the frames of the trimmed videos. Finally all the frames will be used to create a GIF.

### B. Step by Step method

#### Trimming the videos

1. Open `createGif.py`

2. Run method `trimVideo(input_video, start_time, end_time)`

3. You have to mention the path of the video as argument along with the start and end time (in seconds) of the part of the video to be trimmed.

#### Extracting Video Frames

1. Open `createGif.py`

2. Run the method `extractVideoFrames(input_video)`

3. Specify the path of the video in the arguments

#### Creating GIF from the extracted frames

1. Open `createGif.py`

2. Run the method `createGIF(path_to_frames)`

3. Specify the path to the extracted frames in the arguments.


## Horizontally merging the GIFs

* If you want to create a Grid of `NxM`, then make `N` horizontal grids each containing `M` Gifs (merged together)

* Merge `M` Gifs using ,`mergeGIFs('H', path to the folder containing M Gifs)`

## Vertically Merging the GIFs

* Merge all the `N` horizontal grids (each containing `M` Gifs) vertically using, `mergeGIFs('H', path to the folder containing N horizontal grid of Gifs)`, to get a final grid of size `NxM`
