import cv2

# load the image
image = cv2.imread('./image.jpg', cv2.IMREAD_COLOR)

glow_strength = 5  # 0: no glow, no maximum, change according to your needs
glow_radius = 15  # blur radius - can't give multiples of 10

blur = cv2.GaussianBlur(image, (glow_radius, glow_radius), 0)
img_blended = cv2.addWeighted(blur, 1, blur, glow_strength, 0)

# Saving the image to a file
cv2.imwrite("./neon.png", img_blended)
