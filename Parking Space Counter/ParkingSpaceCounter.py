import cv2
import pickle
import cvzone
import numpy as np

#The video feed
cap = cv2.VideoCapture('carPark.mp4')


# we need to import of all the positions that we have loaded
# the car positions the same was as the other file

with open("Parking Space Counter\CarParkPos", 'rb') as f:  # adds to the pickle object - Opens file with read privileges
    posList = pickle.load(f)

width, height = 107, 48                         # The dimensions of a parking space

def checkParkingSpace(imgProcessed):

    spaceCounter = 0

    for pos in posList:

        x, y = pos
        # we need to determine whether there is a car in the position
        imgCrop = imgProcessed[y:y+height, x:x+width]
        # The square brackets are used to slice a portion of the 2D image array
        # cv2.imshow(str(x*y), imgCrop)  # This just shows us one of the parking spaces
        # The drawing must be done after the crop to avoid the purple rectangle in the cropped image
        # We must count the pixels to determine whether there is a car in the parking space
        # A high count will indicate car, low count will indicate no car.
        count = cv2.countNonZero(imgCrop)
        # Lets write the count number infront of the box so that we can set a threshold
        cvzone.putTextRect(img, str(count), (x, y+height - 3), scale = 1, thickness=1, offset = 0, colorR=(0, 0, 255))
        # imgProcessed = cv2.putText(img, 'OpenCV', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        if count < 800:
            # Change the colour to show the space is free
            colour = (0,255,0)
            thickness = 5
            spaceCounter += 1
        else:
            colour = (0,0,255)
            thickness = 2
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), colour, thickness)

    cvzone.putTextRect(img, f'There are currently {spaceCounter}/ {len(posList)} spaces free', (100, 50), scale=2,
                       thickness=4, offset=20, colorR=(0, 200, 0))

# To determine whether there is a car present or not we need to look at the pixel count of the box
# We can turn it into a binary image, if it is a plane image there is no car, otherwise there is a car


while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):  # We want to loop the video so that we dont have to keep opening it
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)     #resets the frame to the start

    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16) # Convert into binary image by using adaptive thresholding
    # Adaptive threshold must have a 1 channel input there it must be turned it grey beforehand
    imgMedian = cv2.medianBlur(imgThreshold,5)  # Kernel size of 5, -- Aiming to get rid of some of the salt and pepper noise
    #use numpy to make a kernel
    kernel = np.ones((3,3),np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations = 1)  # Dilation causes the white areas to increase in width


    checkParkingSpace(imgDilate)
    #for pos in posList:

    cv2.imshow('Image', img)     # opens the video
    # cv2.imshow('Gray', imgGray)     # opens the video in gray
    # cv2.imshow('Blur', imgBlur)     # opens the video blurred
    # cv2.imshow('Thresh', imgThreshold)     # opens the video as a binary video
    # cv2.imshow('Median', imgMedian)       # Shows after the median blur - Gets rid of salt and pepper noise
    # cv2.imshow('Dilated', imgDilate)        # Shows the image after dilation - increases width of white areas
    cv2.waitKey(10)          # 10ms delay - Slows it down

