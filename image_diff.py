# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:14:53 2018

This is from Adrian Rosebrock from his website
https://www.pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/
"""

#import required libraries
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2

#arguments parsing for first input image and second input image
#ap = argparse.ArgumentParser()
#ap.add_argument("-f", "--first", required = True, help = "first input image")
#ap.add_argument("-s", "--second", required = True, help = "second")
#args = vars(ap.parse_args())

#Load Images MAKE SURE THEY HAVE THE SAME DIMENSIONS
path1 = (r"C:\Users\Reaper124\.spyder-py3\Scripts\ImageComparison\visa.png")
path2 = (r"C:\Users\Reaper124\.spyder-py3\Scripts\ImageComparison\new-mastercard.png")

#load input images
imageA = cv2.imread(path1)
imageB = cv2.imread(path2)

#Convert images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

#compute the structural similarity index (SSI) between the images
#ensuring that the difference is returned
(score, diff) = compare_ssim(grayA, grayB, full = True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))

#Threshold the difference image followed by contours to find the differences
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

#loop over contours
for c in cnts:
    #This computes the bounding box
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

#show the image differences 
cv2.imshow("Original", imageA)
cv2.imshow("Modified", imageB)
cv2.imshow("Diff", diff)
cv2.imshow("Threshold Image", thresh)
cv2.waitKey(0)

