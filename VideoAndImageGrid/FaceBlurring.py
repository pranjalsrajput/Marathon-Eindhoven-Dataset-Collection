# Python Program to blur image

# Importing cv2 module
import cv2

# bat.jpg is the batman image.
img = cv2.imread('/home/pranjal/Documents/Assignments/Deep Learning Project/NewDataset/Videos For Sample/35/Frames/VID_20191013_131503695_trimmed_8.jpg')



# make sure that you have saved it in the same folder
# Averaging
# You can change the kernel size as you want
# avging = cv2.blur(img, (10, 10))
# cv2.imshow('Averaging', avging)
# cv2.imwrite('/home/pranjal/Documents/Assignments/Deep Learning Project/NewDataset/Videos For Sample/35/Frames/testavging.jpg',avging)
# cv2.waitKey(0)

# Gaussian Blurring
# Again, you can change the kernel size
gausBlur = cv2.GaussianBlur(img, (9, 9), 0)
cv2.imshow('Gaussian Blurring', gausBlur)
cv2.imwrite('/home/pranjal/Documents/Assignments/Deep Learning Project/NewDataset/Videos For Sample/35/Frames/testCompress1.jpg',gausBlur,[cv2.IMWRITE_JPEG_QUALITY, 59])
cv2.waitKey(0)

# Median blurring
# medBlur = cv2.medianBlur(img, 9)
# cv2.imshow('Media Blurring', medBlur)
# cv2.imwrite('/home/pranjal/Documents/Assignments/Deep Learning Project/NewDataset/Videos For Sample/35/Frames/testmedBlur.jpg',medBlur)
# cv2.waitKey(0)

# Bilateral Filtering
# bilFilter = cv2.bilateralFilter(img, 9, 75, 75)
# cv2.imshow('Bilateral Filtering', bilFilter)
# cv2.imwrite('/home/pranjal/Documents/Assignments/Deep Learning Project/NewDataset/Videos For Sample/35/Frames/testbilFilter.jpg',bilFilter)
# cv2.waitKey(0)
cv2.destroyAllWindows()