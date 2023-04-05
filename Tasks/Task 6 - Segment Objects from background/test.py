import cv2
import numpy as np

# Define a function to be called when the trackbar value is changed
def update_binary_threshold(val):
    # Get the current trackbar value
    threshold = cv2.getTrackbarPos('Threshold', 'Binary Image')

    # Apply binary thresholding with the specified threshold value
    _, binary_img = cv2.threshold(resized, threshold, 255, cv2.THRESH_BINARY)

    # Display the binary image
    cv2.imshow('Binary Image', binary_img)

# Load the image
image = cv2.imread('Tasks\Task 6 - Segment Objects from background\image.jpg', cv2.IMREAD_GRAYSCALE)
resized = cv2.resize(image, (0,0), fx=0.25, fy=0.25)
# Create a window to display the binary image
cv2.namedWindow('Binary Image')

# Create a trackbar to adjust the binary threshold value
cv2.createTrackbar('Threshold', 'Binary Image', 128, 255, update_binary_threshold)

# Call the update_binary_threshold function once to display the initial binary image
update_binary_threshold(128)

# Wait for a key to be pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
