# ImageDifference_StructuralSimilarityIndex
Show differences between two images and establish a SSIM</br>
Process:</br>
1)Verify both images are the same dimensions (x,y). </br>
If (dim(path1)==dim(path2)): proceed to step 3</br>
Else:proceed to step 2</br>
2)Utilize imageResize.py to convert to smallest dimension of the two images and rename </br>
3)Updated path1 and path2 directories to your local image paths within image_diff.py </br>
4)Run image_diff.py
