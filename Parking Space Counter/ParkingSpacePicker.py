# First we need to open up our image and mark each parking space as a region of interest
# A for loop can not be used because the car parking is not directly above the image, does not allow for the trolley
# parking spaces and there is other irregularities

# Create the parking spaces and put them into a list and send them to the main code

import cv2
import pickle


width, height = 107, 48                         # The dimensions of a parking space

try:
    with open("CarParkPos", 'rb') as f:  # adds to the pickle object - Opens file with read privileges
        posList = pickle.load(f)
except:
    posList = []                                    # List for the positions of the parking spaces


def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1+width and y1 < y < y1+height:
                posList.pop(i)

    with open("CarParkPos", 'wb') as f:     #adds to the pickle object
        pickle.dump(posList, f)             #dumps the position list in the file "CarParkPos"


while True:

    img = cv2.imread("carParkIMG.png")  # Load the image and save into variable img

    for pos in posList:
        cv2.rectangle(img, pos, (pos[0]+width, pos[1] + height), (255, 0, 255), 2)



    #cv2.rectangle(img,(50, 192), (150,145), (255,0,255), 2 )    # Draw a rectangle around the 2nd parking space on left
    cv2.imshow("Image", img)                                    # Show the image
    cv2.setMouseCallback("Image", mouseClick)
    cv2.waitKey(1)

