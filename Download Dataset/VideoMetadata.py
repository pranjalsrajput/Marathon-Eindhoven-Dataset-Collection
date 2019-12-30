import exiftool
import xlsxwriter
import os
import sys

workbook=xlsxwriter.Workbook("video_metadata.xlsx")
worksheet= workbook.add_worksheet("Metadata")
row=0
col=0

columnNames=["FileName","FileSize","FileType","Duration","VideoFrameRate","ImageSize","TrackCreateDate","GPSCoordinates"]
for i in range(len(columnNames)):
    worksheet.write(row, col+i, columnNames[i])

#dataLocation=str(sys.argv[1])
mypath="./"
#dataLocation="/home/pranjal/Documents/Assignments/Deep Learning Project/"
textfilename="listOfVideos.txt"
with open(mypath+textfilename) as f:
  for line in f:
      videopath = line
      print(videopath)
      files = [videopath]
      row += 1
      col = 0
      with exiftool.ExifTool() as et:
          metadata = et.get_metadata_batch(files)
      for data in metadata:
          #print("data: ", data)
          if "File:FileName" in data:
              worksheet.write(row, col, videopath)
          if "File:FileSize" in data:
              worksheet.write(row, col + 1, data["File:FileSize"]/(1024*1024))
          if "File:FileType" in data:
              worksheet.write(row, col + 2, data["File:FileType"])
          if "QuickTime:Duration" in data:
              worksheet.write(row, col + 3, round(data["QuickTime:Duration"],2))
          if "QuickTime:VideoFrameRate" in data:
              worksheet.write(row, col + 4, round(data["QuickTime:VideoFrameRate"]))
          if "Composite:ImageSize" in data:
              worksheet.write(row, col + 5, data["Composite:ImageSize"])
          if "QuickTime:TrackCreateDate" in data:
              worksheet.write(row, col + 6, data["QuickTime:TrackCreateDate"])
          if "QuickTime:GPSCoordinates" in data:
              worksheet.write(row, col + 7, data["QuickTime:GPSCoordinates"])
          else:
              worksheet.write(row, col + 7, "-")
workbook.close()
