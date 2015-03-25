import cv2 as cv

"""
This script contains auxilary functions to be used during development.
Functions contained in this script probably won't be necessary in the product's
integration.
"""

def save_img(image, output_name, question):

    print question
    ans = raw_input()

    # Checks that the input is within the correct values
    ans_list = ["y", "yes", "n", "no", "Y", "YES", "N", "NO"]
    while ans not in ans_list:
        print question
        ans = raw_input()

    # Saving the thresholded image
    if ans[0] == 'y' or ans[0] == 'Y':
        print "Saving..."
        cv.imwrite(output_name, image)
        print "Saved as {0}.".format(current_out_name)

    return 0
