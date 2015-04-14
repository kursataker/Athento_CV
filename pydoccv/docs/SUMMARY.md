This file contains a basic description of each function included in the
PyDocCV package and their common parameters and error codes, as a basic guide to 
use it in the CLI .

##Common parameters

    - input_file: input file path
    - thresh_val: list of values used to threshold.
    - quality: quality to use in the pdf_to_png transformation.
    - window_size: size of the window used to blur. As this values increases so
                    does the blur.
    - kernel_size: size of the kernel used to blur. As this values increases so
                    does the blur.

##Summary

Each module name identifies the kind of operation that can be performed with the
 functions within the modules:

- **bg_color**:  transforms the image into grayscale and applies a series
 of threshold values to the image if none is indicated by parameter. Functions:

    ```clean(input_file, thresh_val =  [225, 220, 215, 210, 205, 200],
                         window_size = 3)```

- **ftm_pyramid**: performs a template matching operation using an approximation
with pyramids to improve it's performance:

    ```ftm_pyramid(input_file, template, max_level = 5)```

- **lines_detection**: analyses the image looking for lines in it. It may remove
them, draw them or return some info about the lines. Lines are detected using the 
HoughLines function. This module has several functions:

    ```detect_lines(image, rho = 1, theta = np.pi/180, threshold = 200):```
    ```delete_lines(image, lines, line_length = 1000, width = 5,
                        color = (255,255,255)):```
    ```delete_all_lines(image, line_length = 1000, width = 5,
                            color = (255, 255, 255)):```
    ```distance(line1, line2, line_length = 1000):```
    ```distance_mean(lines, line_length = 1000):```
    ```draw_lines(image, lines, line_length = 1000, width=5, 
                        color=(0,0,255)):```
    ```get_line_coordinates(line, line_length = 1000):```
    ```line_count(lines, line_length = 1000, error = 5):```
    ```parallels(line1, line2, line_length = 1000, error = 5):```


- **lines_detection_p**: equivalent to lines_detection but using a probabilistic
approach.  Lines are detected using the HoughLinesP function. This module has 
several functions:

    ```detect_lines(image, minLineLength = 30, maxLineGap = 20, rho = 1,
                 theta = np.pi/180, threshold = 200)```
    ```delete_all_lines(image, width = 5, color = (255, 255, 255))```
    ```delete_lines(image, lines, width = 5, color = (255,255,255))```
    ```distance(line1, line2)```
    ```distance_mean(lines, line_length = 1000)```
    ```draw_lines(image, lines, width = 5, color = (0,0,255))```
    ```line_count(lines, error = 5)```
    ```parallels(line1, line2, error = 5)```

- **salt_pepper**: transforms the image into grayscale and performs a complete 
erode operation. This is used to improve the quality of the text when it has 
much “salt and pepper” noise. Functions:

    ```clean(input_file,  thresh_val = [250, 245, 240, 230, 225, 220], 
                window_size = 5, kernel_size = 5)```

- **threshold**: applies a series of threshold values to an input image. 
    Functions:
    
    ```apply(image, thresh_values, output_name)```


##Use in CLI

Some of the functions described below may be used directly in the CLI. In order 
to know how to properly use the commands, open a terminal and navigate to the 
*pydoccv* folder and type:

    ```python bg_color.py -h```
    ```python ftm_pyramid.py -h```
    ```python lines_detection.py -h```
    ```python lines_detection_p.py -h```
    ```python salt_pepper.py -h```
    ```python threshold.py -h```
    
    

#FILE DESCRIPTIONS


##bg_color

This script allows to clean an image with noisy background (ie: coloured 
background).

Once it receives the parameters, it transforms the image to grayscale and 
applies a Gaussian Blur to the image. 
        
In the end, it applies a series of threshold values (or the ones received by 
parameter) to the modified image and shows them asking the user to save the the 
current thresholded image.
                       
Returns:
The original image thresholded in a series of values. The output image will be 
saved as:
                
    input_name-GREY-(V)THRESH, where (V) is the value of the applied threshold.
                
Use in CLI:
    python bg_color.py -i myImage.png
    python bg_color.py -i myImage.png -t X, where X is the threshold value
    python bg_color.py -i myImage.png -w X, where X is the size of the window 
                                                used in the Gaussian Blur.
                
As usual, you can use any combination of parameters that you may need.
        
Import:
To import this function into your application, you must include the following 
line at the beginning:
    ```from bg_color import clean```
    

##ftm_pyramid




##lines_detection

This script allow to perform several operations in documents that contain lines.

Common parameters:
    - image: the image to perform lines operations on it.
    - lines: a list of lines.
    - lineX: where X is a number. A single line.
    - line_length: the length of each line of the image.
    - width: the width of the line drawn.
    - color: the colour of the line drawn.
    - error: a margin of error of deviation of the lines. Sometimes not every
             pixel on a line is recognized as part of one, resulting in lines
             that may move some coordinates a few pixels even if the line is
              vertical or horizontal. On pixels.
              
Operations supported:


####detect_lines(image, rho = 1, theta = np.pi/180, threshold = 200)

Uses the HoughLines function to detect lines in an image.

Arguments:

    - rho:
    
    - theta:
    
    - threshold
    
Returns:
    
    A list of lines (each line is a set of coordinates).


####delete_lines(image, lines, line_length = 1000, width = 5, color = (255,255,255)):

Deletes the lines received by drawing them in the same color as the document's
background.
    
Returns:
    
    A new image which is the input image with the lines drawn in the selected 
    colour.

    
####delete_all_lines(image, line_length = 1000, width = 5, color = (255, 255, 255)):

Uses the delete_lines function in a loop to delete all lines detected until no
more lines can be found in the image. Same arguments and return as delete_lines.


####distance(line1, line2, line_length = 1000):

Calculates the absolute distance between two lines that must be parallels.

Returns:
    
    A list of two elements [x,y], which are the distance in pixels between two
    coordinates of the lines.

    
####distance_mean(lines, line_length = 1000):

Calculates the mean distance between a set of lines.

Returns:

    The mean of the distance between each line.


####draw_lines(image, lines, line_length = 1000, width=5, color=(0,0,255)):

Draws the lines into the input image in the selected colour.
    
Returns:

    A new image which is the input image with the input lines drawn on it in the
    selected colour.
    

####get_line_coordinates(line, line_length = 1000):

Calculates the coordinates of the line received given a line length.
    
Returns:

    [x1, y1, x2, y2] a set of coordinates that represents the line.
   
    
####line_count(lines, line_length = 1000, error = 5):

Counts the total of lines, and checks how many horizontal and vertical lines are.
A line is considered horizontal or vertical if it's coordinates (Y or X 
respectively) is constant (+- error argument value).
    
Returns:

    [total, num_vertical_lines, num_horizontal_lines]


####parallels(line1, line2, line_length = 1000, error = 5):

Checks if two lines are parallels, within an expected margin of error in pixels.

Returns:

    True or false.



##lines_detection_p




##salt_pepper

This script cleans an image with white noise (ie: text dotted due to bad pixel 
definition).

Once it receives the necessary parameters, it transforms the image into gray-
scale and applies a Gaussian Blur + a Median Blur to get extra definition to the 
text. After getting extra pixels for the letters, we use the function erode to 
outline the text in order to improve the quality of the data readed by OCR.
        
In the end, it applies a series of threshold values (or the ones received by 
parameter) to the modified image and shows them one by one asking the user to 
save the current thresholded image.
        
Returns:
    The input image with a blur and median filter in a series with different 
    threshold values.
                
Use in CLI:
    python clean_erode.py -i myImage.png
    python clean_erode.py -i myImage.png -t X, X = threshold value.
    python clean_erode.py -i myImage.png -k X, X = kernel size used in the erode
                                                     function.
    python clean_erode.py -i myImage.png -w X, where X is the size of the window
                                                     used in the Gaussian Blur.
                
    As usual, you can use any combination of parameters that you may need.
        
Import:
    To import this function into your application, you must include the follo-
    wing line at the beginning:

    ```from clean_erode import clean```


##threshold

This function applies a series of threshold values (or the ones received by 
parameter) to the modified image and shows them asking the user to save the the 
current thresholded.

The output images are saved in the same directory as the source.

Returns: 0 if everything works fine.
    
Use in CLI
    python threshold.py -i myImage.png
    python threshold.py -i myImage.png -t X, where X is the threshold value
    python threshold.py -i myImage.png -o N, where N is the custom name for the
                                            output without the file extension.

Import:
    To import this function into your application, you must include the following 
    line at the beginning:
    
    ```from threshold import apply```
