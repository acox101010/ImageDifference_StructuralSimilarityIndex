# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 18:06:09 2018

@author: Reaper124
"""
#import PIL and resizeimage"
from PIL import Image
from resizeimage import resizeimage

#load file path
im_path = (r"C:\Users\Reaper124\.spyder-py3\Scripts\ImageComparison\mastercard.png")

with open(im_path, 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [393, 292])#adjust end dimensions
        cover.save('new-mastercard.png', image.format)#rename your new file in argument 0
