import cv2 as cv
import numpy as np
import os


def detect_lines(image, rho = 1, theta = np.pi/180, threshold = 200):

    print image.shape
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize = 3)
    lines = cv.HoughLines(edges, rho, theta, threshold)
    return lines


def delete_lines(image, lines, line_length = 1000, color = (255,255,255),
                   width = 5):

    return draw_lines(image, lines, line_length, color, width)


def delete_all_lines(image, line_length = 1000, color = (255, 255, 255),
                     width = 5):

    lines = detect_lines(image)
    while lines != None:
        image = delete_lines(image, lines, line_length, color, width)
        lines = detect_lines(image)

    return image


def distance(line1, line2, line_length = 1000):

    res = -1
    if parallels(line1, line2):
        l1_x1, l1_y1, l1_x2, l1_y2 = get_line_coordinates(line1, line_length)
        l2_x1, l2_y1, l2_x2, l2_y2 = get_line_coordinates(line2, line_length)
        res = [abs(l1_x1 - l2_x1), abs(l1_y1 - l2_y1)]

    return res


def distance_mean(lines, line_length = 1000):
    n_lines = np.size(lines)
    total = [0, 0]
    for l1 in lines[0]:
        for l2 in lines[0]:
            d = distance(l1, l2, line_length)
            if d != -1:
                total[0] += d[0]
                total[1] += d[1]

    return [total[0]/n_lines, total[1]/n_lines]


def draw_lines(image, lines, line_length = 1000, color=(0,0,255), width=5):

    for l in lines[0]:
        x1, y1, x2, y2 = get_line_coordinates(l, line_length)
        cv.line(image, (x1, y1), (x2, y2), color, width)

    return image


def get_line_coordinates(line, line_length = 1000):

    rho, theta = line
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + line_length*(-b))
    y1 = int(y0 + line_length*(a))
    x2 = int(x0 - line_length*(-b))
    y2 = int(y0 - line_length*(a))

    return [x1, y1, x2, y2]


def line_count(lines, line_length = 1000, error = 5):

    total = 0
    v_lines = 0
    h_lines = 0

    for l in lines[0]:
        x1, y1, x2, y2 = get_line_coordinates(l, line_length)
        if x1 in range(x2-error, x2+error):
            v_lines += 1
        elif y1 in range (y2-error, y2+error):
            h_lines += 1
        total += 1

    return [total, v_lines, h_lines]


def parallels(line1, line2, line_length = 1000, error = 5):

    l1_x1, l1_y1, l1_x2, l1_y2 = get_line_coordinates(line1, line_length)
    l2_x1, l2_y1, l2_x2, l2_y2 = get_line_coordinates(line2, line_length)

    return (l1_x1 - l2_x1 in range(
        (l1_x2 - l2_x2 - error), (l1_x2 - l2_x2 + error))) and \
           (l1_y1 - l2_y1 in range(
        (l1_y2 - l2_y2 - error), (l1_y2 - l2_y2 + error)))




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
