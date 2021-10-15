import cv2

# read the image
image = cv2.imread("images/image.jpg")

# creating the pencil sketch directly
image_out = cv2.pencilSketch(image, sigma_s=60, sigma_r=0.07, shade_factor=0.05)

# save the images
cv2.imwrite("images/sketch.jpg", image_out[0])
cv2.imwrite("images/sketch-color.jpg", image_out[1])
