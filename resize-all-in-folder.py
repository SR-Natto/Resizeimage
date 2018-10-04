import cv2
import os 
import numpy


mypath='C:/Users/Nattaphon/Desktop/new/batman'
     
for filename in os.listdir(mypath): 

    # read image
    img = cv2.imread(mypath+'/'+filename, cv2.IMREAD_UNCHANGED)
    # get dimensions of image
    dimensions = img.shape

    # height, width, number of channels in image
    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]

    if width <= 300 or height <=150 :
        img = cv2.resize(img,(300,150)) 
        print ('Small is resize')
        
    elif width >=600 or height >=300 :
        img = cv2.resize(img,(600,300))

        print ('Big is resize')

    cv2.imwrite( filename+'.jpg',img )
    #print('Image Dimension    : ',dimensions)
    #print('Image Height       : ',height)
    #print('Image Width        : ',width)
    #print('Number of Channels : ',channels
