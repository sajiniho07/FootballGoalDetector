# Football Goal Detection
<br>

## About
### Hough circle method
This Python project uses OpenCV to detect whether a goal is present in a series of images. It does this by identifying circles in the images that match the size and shape of a football goal, and then checking if they are located above or below a line that is drawn based on the position of the goalposts.

## Installation

```
pip install opencv-python
pip install numpy
```

## Usage

### Hough circle method
The FootballGoalDetection class has three methods:

- __init__(): Initializes the object and sets the sensitive area and m & b of the goalpost lines.
- get_image_and_processed_edges(name): Returns the resized image and the edges processed from it.
- is_goal_detected(x_cent, y_cent, radius): Returns True if the circle detected inside the goalpost region is determined to be a goal, False otherwise.
- goal_detector(): Loops through a series of images, detects circles using the HoughCircles function in OpenCV, and checks if the detected circles are goals.

By default, this will loop through six images (res/1.jpg through res/6.jpg) and print a message to the console when a goal is detected.
Sample:
```
Goal detected in frame name: 6
or
No Goal detected.
```

## License ##

Made with :heart: by <a href="https://github.com/sajiniho07" target="_blank">Sajad Kamali</a>

<a href="#top">Back to top</a>
