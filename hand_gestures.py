import math
import cv2
import numpy as np
import pyautogui


cap = cv2.VideoCapture(0)  #(device 0) this guuantes you use your default webcam
if not cap.isOpened():
    print("Error: My webcam could not open ! Hellllp!")
    exit()

# define ROI(region of interest) coordinates for hand appearance tracking (x, y, r_width, r_height)
roi_x, roi_y, roi_w, roi_h = 100, 100, 300, 300

# now we read a preprocess each frame with a simple while loop!
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame if needed
    frame = cv2.flip(frame, 1)

    # Optionally extract ROI:
    roi = frame[roi_y:roi_y+roi_h, roi_x:roi_x+roi_w]

    # cont. processing on 'roi'
# but first! we convert ROI to HSV color space
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# create a mask for ethical consideration(skin colors)
lower_skin = np.array([0, 20, 70], dtype=np.uint8)
upper_skin = np.array([20, 255, 255], dtype=np.uint8)
mask = cv2.inRange(hsv, lower_skin, upper_skin)

# Create a threshold for the image
ret, thresh = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)

# Find contours if any in image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
if contours:
    contour = max(contours, key=lambda x: cv2.contourArea(x))
else:
    continue  # if no contours are detected skip the frame for efficiency

# draw the quadrilateral bounds
x, y, w, h = cv2.boundingRect(contour)
cv2.rectangle(roi, (x, y), (x+w, y+h), (0, 0, 255), 2)

#Compute Convex Hull and Draw Contours
hull = cv2.convexHull(contour)
cv2.drawContours(roi, [contour], -1, (0, 255, 0), 2)
cv2.drawContours(roi, [hull], -1, (0, 0, 255), 2)

#Find Convexity Defects
hull_indices = cv2.convexHull(contour, returnPoints=False)
if len(hull_indices) > 3:  # At least 3 points required for defects
    defects = cv2.convexityDefects(contour, hull_indices)
else:
    defects = None

# create/initialize a defect counter
count_Defects = 0

#Analyze Each Defect to Detect Fingers
if defects is not None:
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(contour[s][0])
        end = tuple(contour[e][0])
        far = tuple(contour[f][0])
        
        # Compute lengths between points
        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
        
        # Apply cosine rule to find the angle
        angle = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        
        # Count defects (i.e., space between fingers)
        if angle <= 90:
            count_Defects += 1
            cv2.circle(roi, far, 4, [0, 0, 255], -1)
        cv2.line(roi, start, end, [0, 255, 0], 2)


if count_Defects >= 4:
    pyautogui.press('space')  # Simulate space bar press
    cv2.putText(frame, "JUMP", (roi_x, roi_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
else:
    # You can define other commands based on defect count if desired
    cv2.putText(frame, f"Defects: {count_Defects}", (roi_x, roi_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)


#show DA WORKK!!! 
cv2.imshow("Threshold", thresh)
cv2.imshow("ROI", roi)
cv2.imshow("Frame", frame)

#figure/handle exit conditions
key = cv2.waitKey(10) & 0xFF
if key == 27:  # ESC key to break out of loop
    break

# when done dont forget to release the video capture
cap.release()
cv2.destroyAllWindows()
