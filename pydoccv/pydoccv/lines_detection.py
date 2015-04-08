import cv2 as cv
import numpy as np
import os


def detect_lines(input_file, minLineLength = 30, maxLineGap = 20, rho = 1,
                 theta = np.pi/180, threshold = 200):

    if file_exists(input_file) == False:
        raise IOError("Input file not found.")

    #image = cv.imread(input_file)

    ##INPUTS TO DELETE
    img = cv.imread("../resources/lines.jpg")
    #img = cv.imread("../resources/lines2.png")

    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize = 3)

    rho = 1
    theta = np.pi/180
    threshold = 200
    minLineLength = 30
    maxLineGap = 20

    lines = cv.HoughLinesP(edges, rho, theta, threshold, minLineLength,
                           maxLineGap)

    return lines


def delete_lines(image, lines, color=(0,0,0), width=5):
    for x1,y1,x2,y2 in lines:
        cv.line(image, (x1,y1), (x2,y2), color, width)
    return image


def draw_lines(image, lines, color=(0,0,255), width=5):
    for x1,y1,x2,y2 in lines:
        cv.line(image, (x1,y1), (x2,y2), color, width)
    return image


def line_count(lines):
    total = 0
    h_lines = 0
    v_lines = 0

    for x1,y1,x2,y2 in lines: #lines[0]
        if x1 == x2:
            v_lines += 1
        if y1 == y2:
            h_lines += 1
        total += 1

    return [total, v_lines, h_lines]


def parallels(line1, line2):
    l1_x1, l1_y1, l1_x2, l1_y2 = line1
    l2_x1, l2_y1, l2_x2, l2_y2 = line2

    return (l1_x1 - l2_x1 == l1_x2 - l2_x2) and (l1_y1 - l2_y1 == l1_y2 - l2_y2)


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
