import argparse
import cv2 as cv
import threshold as th
import os

"""
This script cleans an image with noisy background, improving the OCR in docu-
ments where the background has a colour.
"""

def clean(input_file, thresh_val =  [225, 220, 215, 210, 205, 200],
                        window_size = 3):
      
        # Ensures that window_size parameter is integer
        window_size = int(window_size)

        #Checking arguments and raising expected exceptions
        check_arguments(input_file, window_size)

        # Loading the image
        image = cv.imread(input_file)
        
        # Grayscale and Gaussian Blur
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        image = cv.GaussianBlur(image, (window_size, window_size), 0)

        # Applying threshold list
        th.apply(image, input_file, thresh_val)
        
        cv.waitKey(0)
        return 0


def check_arguments(input_file, window_size):
    if input_file == '':
        raise IOError("Input file can't be ''.")

    if input_file == None:
        raise IOError("Input file can't be None.")

    if os.path.isfile(input_file) == False:
        raise IOError("Input file not found.")

    if window_size < 0:
        raise ValueError("Window size value must be greater than 0")

    if window_size % 2 == 0:
        raise ValueError("Window size value must be odd.")
    return 0

if __name__ == '__main__':
        
        # CLI arguments
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--input", required="True", 
                        help="Path to the input file.")
        ap.add_argument("-t", "--threshold", 
                        help="Pixel value to threshold.")
        ap.add_argument("-w", "--windowsize", 
                        help="Odd value, size of the window used in the \
                        Gaussian Blur.")
        args = vars(ap.parse_args())


        # Loading values
        input_file = args["input"]
        thresh_val = args["threshold"]
        window_size = args["windowsize"]
        
        # Setting values:
        if thresh_val == None:
                thresh_val = [225, 220, 215, 210, 205, 200]
        else:
                thresh_val = [thresh_val]
        
        if window_size == None:
	        window_size = 3
        
        clean(input_file, thresh_val, window_size)

