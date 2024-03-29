# -*- coding: utf-8 -*-
"""cameraCalibration.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17rlhNefEET5_qONxXqpBp-Nk2BjM6eAH
"""

import cv2 as cv
import os

CHESS_BOARD_DIM = (9, 6)
n = 0  # image counter

# Checking if the images directory exists, if not then create the images directory
image_dir_path = "images"

if not os.path.isdir(image_dir_path):
    os.makedirs(image_dir_path)
    print(f'"{image_dir_path}" directory is created.')
else:
    print(f'"{image_dir_path}" directory already exists.')

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

def detect_checker_board(image, gray_image, criteria, board_dimension):
    ret, corners = cv.findChessboardCorners(gray_image, board_dimension)
    if ret == True:
        corners1 = cv.cornerSubPix(gray_image, corners, (3, 3), (-1, -1), criteria)
        image = cv.drawChessboardCorners(image, board_dimension, corners_subpix, ret)
    return image, ret

cap = cv.VideoCapture(0)
while True:
    frame = cap.read()
    copy_Frame = frame.copy()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    image, board_detected = detect_checker_board(frame, gray, criteria, CHESS_BOARD_DIM)

    # Add text to the frame
    cv.putText(frame, f"saved_img : {n}", (30, 40), cv.FONT_HERSHEY_PLAIN, 1.4, (0, 255, 0), 2, cv.LINE_AA)

    cv.imshow("frame", frame)
  #  cv.imshow("copyFrame", copy_frame)

    key = cv.waitKey(1)

    if key == ord("q"):
        break
    if key == ord("s") and board_detected == True:
        # Save the checkerboard image
        #cv.imwrite(f"{image_dir_path}/image_{n}.png", copy_frame)
        print(f"Saved image number {n}")
        n += 1  # Increment the image counter

cap.release()
cv.destroyAllWindows()

print("Total saved images:", n)