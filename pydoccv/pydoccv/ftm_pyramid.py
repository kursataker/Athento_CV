import cv2 as cv
import numpy as np
import argparse
import os

"""
This script performs a fast template matching algorithm using the OpenCV
function matchTemplate plus an approximation through pyramid construction to
improve it's performance on large images.
"""

def buildPyramid(image, max_level):

    results = [image]
    aux = image

    for i in range(0,max_level):
        aux = cv.pyrDown(aux)
        results = [aux] + results

    return results


def temp_match(input, template, max_level):

    results = []

    source_pyr = buildPyramid(input, max_level)
    template_pyr = buildPyramid(template, max_level)

    for lvl in range(0, int(max_level), 1):

        curr_image = source_pyr[lvl]
        curr_template = template_pyr[lvl]

        dX = curr_image.shape[1] + 1 - curr_template.shape[1]
        dY = curr_image.shape[0] + 1 - curr_template.shape[0]

        result = np.zeros([dX, dY])


        #On the first level performs regular template matching.
        if lvl == 0:
            result = cv.matchTemplate(curr_image, curr_template,
                                      cv.TM_CCORR_NORMED)

        #On every other level, perform pyramid transformation and template
        #matching on the predefined ROI areas, obtained using the result of the
        #previous level.
        else:
            mask = cv.pyrUp(r)

            mask8u = cv.inRange(mask, 0, 255)
            contours = cv.findContours(mask8u, cv.RETR_EXTERNAL,
                                       cv.CHAIN_APPROX_NONE)

            #Uses contours to define the region of interest and perform TM on
            #the areas.

            for i in range(0, np.size(contours)-1):
                x, y, w, h = cv.boundingRect(contours[i][0])
                tpl_X = curr_template.shape[1]
                tpl_Y = curr_template.shape[0]

                #result = cv.matchTemplate(curr_image, curr_template,
                #                          cv.TM_CCORR_NORMED)

                result[y:y+h, x:x+w] = cv.matchTemplate(
                                curr_image[y:y+h+tpl_Y, x:x+w+tpl_X],
                                curr_template, cv.TM_CCORR_NORMED)

        T, r = cv.threshold(result, 0.94, 1., cv.THRESH_TOZERO)
        cv.imshow("test", r)
        cv.waitKey()
        results.append(r)
    return results


def ftm_pyramid(input_file, template_file, max_level = 5):

    if file_exists(input_file) == False:
        raise IOError("Input file not found.")

    if file_exists(template_file) == False:
        raise IOError("Input file not found.")

    img = cv.imread(input_file)
    tpl = cv.imread(template_file)

    image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    template = cv.cvtColor(tpl, cv.COLOR_BGR2GRAY)

    tm_results = temp_match(image, template, max_level)

    c = 0
    flag = False

    while flag == False and c < np.size(tm_results):
        current = tm_results[c]
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(current)
        if max_val > 0.9:
            cv.rectangle(img,
                        max_loc,
                        (max_loc[0] + template.shape[1],
                         max_loc[1] + template.shape[0]),
                        (0,0,255), 2)
        else:
            flag = True

        c = c+1

    cv.imshow("Result", img)
    cv.waitKey()
    return 0


# Auxiliary methods

def file_exists(input_file):
    """
    :param input_file: path to the input file
    :return: true or false wether the file exists or not.
    """
    if input_file == '':
        raise ValueError("The input file can't be ''.")
    if input_file == None:
        raise ValueError("The input file can't be a None object")

    return os.path.isfile(input_file)


if __name__ == '__main__':
    #CLI arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required="True",
                    help="Path to the input image.")
    ap.add_argument("-t", "--template", required="True",
                    help="Path to the template image.")
    ap.add_argument("-l", "--levels", help="Number of levels of the pyramid.")
    args = vars(ap.parse_args())

    #Loading values
    input_file = args["input"]
    template = args["template"]
    max_lvl = args["levels"]

    if max_lvl == None:
        max_lvl = 5

    ftm_pyramid(input_file, template, max_lvl)