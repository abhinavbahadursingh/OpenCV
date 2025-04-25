import cv2 as cv

# img = cv.imread('photo/dog.jpg')
# resize_img = rescaleFrame(img)
# cv.imshow('Dog' , resize_img)
# cv.waitKey(0)
# cv.destroyAllWindows()
# cv.imshow('Dog' , resize_img)
def rescaleFrame(frame, fixed_height=1000):
    # Get original dimensions
    height, width = frame.shape[:2]

    # Calculate the new width to maintain aspect ratio
    aspect_ratio = width / height
    new_width = int(fixed_height * aspect_ratio)

    # Resize the image
    dimensions = (new_width, fixed_height)  # Fixed height, proportional width
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)




def changeRes(width , height):
    capture.set(3,width)
    capture.set(4,height)


# reading videos

capture = cv.VideoCapture(0)


changeRes(640 , 480)
while True:
    isTrue , frame = capture.read()
    cv.imshow('video'  , frame)
    # cv.imshow('video resized'  , )
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()