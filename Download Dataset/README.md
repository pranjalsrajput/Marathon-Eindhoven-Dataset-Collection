## Extracting the dataset from zip

A bash Script to download all the ZIP files containing the data and unzip them in the specified destination.

* Run `./bash_unzip` in the terminal

## Downloading the data from a remote server into the local machine

* Mention the list of all files in `listOfZip.txt`
* Mention the path of the destination folder in the bash script `bash_read_listOfZip`
* Run `./bash_read_listOfZip` from the terminal to download all the data in local machine

## Extracting metadata from Videos

* Run `./bash_retrieve_video_info` from the parent folder containing all the videos, you want to extract the metadata of.
* It will generate 2 files namely `listOfVideos.txt` and `video_metadata.xlsx`.
* Always delete these 2 files first, before running the script again.
* Use `ChartAndStats.py` to analyse the extracted metadata and visualize it graphically.
