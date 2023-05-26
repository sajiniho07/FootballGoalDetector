# Football Goal Detection

## About
### Hough circle method
This Python project uses OpenCV to detect whether a goal is present in a series of images. It does this by identifying circles in the images that match the size and shape of a football goal, and then checking if they are located above or below a line that is drawn based on the position of the goalposts.

### YOLO method
This project contains a Python script that implements an algorithm to detect a football goal in a video sequence. The algorithm uses computer vision techniques and object detection models to identify the goalposts and crossbar of a football goal.

## Installation

The following libraries are required to run the script:

- opencv-python
- numpy
- ultralytics

You can install them using pip:
```
pip install opencv-python numpy ultralytics
```

## Usage

### Hough circle method
The FootballGoalDetection class has three methods:

- __init__(): Initializes the object and sets the sensitive area and m & b of the goalpost lines.
- get_image_and_processed_edges(name): Returns the resized image and the edges processed from it.
- is_goal_detected(x_cent, y_cent, radius): Returns True if the circle detected inside the goalpost region is determined to be a goal, False otherwise.
- goal_detector(): Loops through a series of images, detects circles using the HoughCircles function in OpenCV, and checks if the detected circles are goals.

### YOLO method
The detection algorithm works as follows:

1- Load an image of a football goal.

2- Convert the image to grayscale.

3- Apply edge detection to the grayscale image.

4- Crop a sensitive area around the goal from the edge-detected image.

5- Apply Hough line detection to the cropped image to find the line that represents the top of the goal.

6- Calculate the slope and y-intercept of the line.

7- For each frame in the video sequence:

- Apply object detection to the frame using the YOLOv5 model.
For each detected object:

- If the object is a goalpost or crossbar, calculate its center and radius.
- If the calculated center and radius indicate that a goal has been scored, print a message indicating which frame contains the goal.
- The algorithm assumes that the camera is stationary and that the goal does not move during the video sequence. It also assumes that the goal is fully visible in each frame of the video sequence.

By default, this will loop through six images (res/1.jpg through res/6.jpg) and print a message to the console when a goal is detected.
Sample:
```
Goal detected in frame name: 6
or
No Goal detected.
```
## Input Sample

![sample](https://github.com/sajiniho07/FootballGoalDetector/blob/master/res/6.jpg)

## License ##

Made with :heart: by <a href="https://github.com/sajiniho07" target="_blank">Sajad Kamali</a>

<a href="#top">Back to top</a>
