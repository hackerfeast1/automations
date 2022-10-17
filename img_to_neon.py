import cv2

# load the image
image = cv2.imread('./color.jpg', cv2.IMREAD_COLOR)

# # convert the image to gray image
# grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # invert the gray image 
# invert = cv2.bitwise_not(image)

# Blurring the inverted image


# # invert the blurred image
# invertedblur = cv2.bitwise_not(blur)

# # removing the inverted blur from grey image
# sketch = cv2.divide(blur, invertedblur, scale=256.0)
glow_strength = 5  # 0: no glow, no maximum
glow_radius = 15  # blur radius - can't given multiples of 10

blur = cv2.GaussianBlur(image, (glow_radius, glow_radius), 0)
img_blended = cv2.addWeighted(blur, 1, blur, glow_strength, 0)

# Saving the image to a file
cv2.imwrite("sketch.png", img_blended)
