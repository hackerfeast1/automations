import cv2


# load the image
image = cv2.imread('Image.jpg')

# convert the image to gray image
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# invert the gray image 
invert = cv2.bitwise_not(grey_img)

# Blurring the inverted image
blur = cv2.GaussianBlur(invert, (21, 21), 0)

# invert the blurred image
invertedblur = cv2.bitwise_not(blur)

# removing the inverted blur from grey image
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

#display the image
cv2.imshow(sketch)

# Saving the image to a file
cv2.imwrite("sketch.png", sketch)
