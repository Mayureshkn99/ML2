import cv2

# Step 1: Get the live video feed from your webcam
cap = cv2.VideoCapture(0)

# Step 2: Fix a scene (the place you want to monitor) and store it as a reference background image
ret, frame = cap.read()
background = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
background = cv2.GaussianBlur(background, (21, 21), 0)

# Step 3: For every frame, check if there is any unwanted object inside the scene you are monitoring
while True:
    ret, frame = cap.read()
    
    # Convert current frame to grayscale and blur it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    # Compute the absolute difference between the current frame and reference background frame
    diff = cv2.absdiff(background, gray)
    
    # Apply a threshold to the difference image
    thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
    
    # Dilate the thresholded image to fill in holes
    thresh = cv2.dilate(thresh, None, iterations=2)
    
    # Find contours in the thresholded image
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Check if there is any disturbance in the scene
    if len(contours) > 0:
        # Output the text "UNSAFE" in red color on the top right of the frame
        cv2.putText(frame, "UNSAFE", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # Draw a bounding box around the disturbed area
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    else:
        # Output the text "SAFE" in green color on the top right of the frame
        cv2.putText(frame, "SAFE", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the resulting frame
    cv2.imshow("Video Feed", frame)
    
    # Press 'q' to quit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Step 5: Save the live feed
cap.release()
cv2.destroyAllWindows()
