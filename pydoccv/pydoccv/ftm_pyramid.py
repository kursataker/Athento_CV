import cv2 as cv
import numpy as np
import argparse
import os

"""
This script performs a fast template matching algorithm using the OpenCV
function matchTemplate plus an approximation through pyramid construction to
improve he performance on larger files.
"""

def buildPyramid(image, max_level):
    results = [image]

    for i in range(0,max_level):
        aux = cv.pyrDown(image)
        results.insert(0, aux)

    return results

def temp_match(input, template, max_level):

    cv.imshow("src", input)
    cv.waitKey()
    results = []

    source_pyr = buildPyramid(input, max_level)
    template_pyr = buildPyramid(template, max_level)
    for lvl in range(int(max_level), -1, -1):

        curr_image = source_pyr[lvl]
        curr_template = template_pyr[lvl]

        print curr_image.shape
        print curr_template.shape
        print (curr_image.shape + curr_template.shape)

        result = np.zeros(np.size(curr_image) +
                          np.size(1) -
                          np.size(curr_template),
                          cv.CV_32FC1)

        #On the first level performs regular template matching.
        if lvl == max_level:
            result = cv.matchTemplate(curr_image, curr_template,
                                      cv.TM_CCORR_NORMED)

        #On every other level, perform pyramid transformation and template
        #matching on the predefined ROI areas, obtained using the result of the
        #previous level.
        else:

            mask = cv.pyrUp(aux)
            cv.imshow("Mask", mask)
            cv.waitKey()
            #mask8u = cv.cvtColor(mask, cv.CV_32SC1)
            mask8u = cv.inRange(mask, 0, 255)
            contours = cv.findContours(mask8u, cv.RETR_EXTERNAL,
                                       cv.CHAIN_APPROX_NONE)

            #Uses contours to define the region of interest and perform TM on
            #the areas.

            for i in range(0, np.size(contours)):
                x, y, w, h = cv.boundingRect(contours[i][0])
                print contours[i][0]
                print x
                print y
                print w
                print h
                print cv.boundingRect(contours[i][0])
                print curr_template.shape
                #INDEX ERROR, RESULT TIENE DIMENSION 1 (ESCALA DE GRISES)
                result[y:y+h, x:x+w] = cv.matchTemplate(
                                curr_image[
                                    #x:x+w,
                                    #y:y+h
                                    x + (curr_template.shape[1]-1):x+w + (curr_template.shape[1]-1),
                                    y + (curr_template.shape[0]-1):y+h + (curr_template.shape[0]-1)
                                ],
                                curr_template,
                                cv.TM_CCORR_NORMED)

        T, aux = cv.threshold(result, 0.94, 1., cv.THRESH_TOZERO)
        cv.imshow("test", aux)
        cv.waitKey()
        results.append(aux)
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

    flag = False
    while flag == False:
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(tm_results)
        if max_val > 0.9:
            cv.rectangle(cv.point(
                            max_loc.x, template.cols, max_loc.y + template.y),
                        (255, 0, 0), 2)

            cv.floodFill(tm_results, max_loc, np.ScalarType(0), 0,
                         np.ScalarType(0.1), np.ScalarType(1.))
        else:
            flag = True

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