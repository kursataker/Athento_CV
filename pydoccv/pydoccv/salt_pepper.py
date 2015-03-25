import cv2 as cv
import os
import argparse
import threshold as th

"""
This script cleans an image with salt and pepper noise, improving the OCR in
documents that present this type of noise. Also, it can be used in the CLI.
"""


def clean(input_file,  thresh_val = [250, 245, 240, 230, 225, 220], 
                window_size = 5, kernel_size = 5):

    # Ensures that both quality and window_size parameters are integers
    window_size = int(window_size)
    kernel_size = int(kernel_size)

    sp_check_arguments(input_file, window_size, kernel_size)

    # Loading the image
    image = cv.imread(input_file)

    # Applying Grayscale, Gaussian and median blur and erode
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    image = cv.GaussianBlur(image, (window_size, window_size), 0)
    image = cv.medianBlur(image, window_size)
    image = cv.erode(image, (kernel_size, kernel_size))

    # Applying threshold list
    th.apply(image, thresh_val, input_file)

    cv.waitKey(0)
    return 0

def sp_check_arguments(input_file, window_size, kernel_size):

    if os.path.isfile(input_file) == False:
        raise IOError("Input file not found")

    if kernel_size < 0 or kernel_size % 2 == 0:
        raise ValueError("Kernel size value must be positive and odd.")

    if window_size < 0 or window_size % 2 == 0:
        raise ValueError("Window size value must be positive and odd.")

    return 0


        
if __name__ == '__main__':
        
        # CLI arguments
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--input", required="True", 
                        help="Path to the input file.")
        ap.add_argument("-t", "--threshold", 
                        help="Pixel value to threshold.")
        ap.add_argument("-k", "--kernelsize", 
                        help="Kernel size used in erode operation.")
        ap.add_argument("-w", "--windowsize", 
                        help="Odd value, size of the window used in the \
                        Gaussian Blur.")
        args = vars(ap.parse_args())
        
        # Loading values
        input_file = args["input"]
        kernel_size = args["kernelsize"]
        thresh_val = args["threshold"]
        window_size = args["windowsize"]
        
        # Checking the input values:
        if thresh_val == None:
                thresh_val = [250, 245, 240, 230, 225, 220]
        
        if window_size == None:
                window_size = 5
        
        if kernel_size == None:
                kernel_size = 5
        
        clean(input_file, thresh_val, window_size, kernel_size)
