import cv2 as cv
import os
import argparse

"""
This script shows the results of applying threshold values to the input image
and ask the user wether he wants to save the outputed image or not. Also, it can
be used in the CLI.
"""

def apply(image, output_name, thresh_values = [250, 245, 240, 230, 225, 220]):

    #If thresh is not a list of values transform it.
    if isinstance(thresh_values, list) == False:
        thresh_values = [thresh_values]

    #Checking arguments and raising expected exceptions
    check_arguments(image, thresh_values, output_name)

    # Gets the filename without the extension
    output_name, ext = os.path.splitext(output_name)
        
    # Shows the image with the current threshold applied and asks the user
    # whether save the sample or not. It keeps asking until all thresh_values
    # have been tested
    for i in thresh_values:
        ## Applies the threshold and plots it
        (T, img_thresh) = cv.threshold(image, float(i), 255, cv.THRESH_BINARY)
        title = "Thresholded at {0}".format(T)
        cv.imshow(title, img_thresh)
        print "Press any key in the image window to continue..."
        cv.waitKey(0)
        ##Saving procedure, replace this block of code if you want to
        ##stablish a new system of image saving.
        question = "Image thresholded at value {0}.".format(T)
        question += "Do you want to save this image? [y/n]:"
                
        current_output_name = output_name
        current_output_name += "-GREY-{0}T{1}".format(int(T), ext)

        #iu.save_img(img_thresh, current_output_name, question)
                
                
    # In order to display properly the images, in each iteration the
    # opened windows must be closed.
    cv.destroyAllWindows()
    return 0


def check_arguments(image, thresh_values, output_name):

    if output_name == '':
        raise ValueError("The value of the output name can't be ''.")

    if output_name == None:
        raise ValueError("The output name can't be a None object.")

    if image == None:
        raise IOError("Input image is None")


    for i, value in enumerate(thresh_values):
        if int(value) < 0 or int(value) > 255:
            raise ValueError("All threshold values must be between 0 and 255")

    return 0


if __name__ == '__main__':
        
        # CLI arguments
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--input", required="True", 
                        help="Path to the input file.")
        ap.add_argument("-t", "--threshold", 
                        help="Pixel value to threshold.")
        ap.add_argument("-o", "--outputname",
                        help="Fix part of the output name.")
        args = vars(ap.parse_args())
        
        # Loading values
        input_file = args["input"]
        thresh_val = args["threshold"]
        output_name = args["output_name"]
        
        # Checking the input values:
        if thresh_val == None:
                thresh_val = [250, 245, 240, 230, 225, 220]
        
        if output_name == None:
                output_name = input_file
        
        apply(input_file, thresh_val, output_name)
