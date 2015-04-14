import cv2 as cv
import numpy as np


def detect_lines(image, minLineLength = 30, maxLineGap = 20, rho = 1,
                 theta = np.pi/180, threshold = 200):

    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize = 3)

    lines = cv.HoughLinesP(edges, rho, theta, threshold, minLineLength,
                           maxLineGap)

    return lines


def delete_lines(image, lines, width = 5, color = (255,255,255)):

    return draw_lines(image, lines, width, color)


def delete_all_lines(image, width = 5, color = (255, 255, 255)):

    lines = detect_lines(image)
    while lines != None:
        image = delete_lines(image, lines, width, color)
        lines = detect_lines(image)

    return image


def distance(line1, line2):

    res = -1
    if parallels(line1, line2):
        l1_x1, l1_y1, l1_x2, l1_y2 = line1
        l2_x1, l2_y1, l2_x2, l2_y2 = line2
        res = [abs(l1_x1 - l2_x1), abs(l1_y1 - l2_y1)]

    return res


def distance_mean(lines):
    n_lines = np.size(lines)
    total = [0, 0]
    for l1 in lines[0]:
        for l2 in lines[l1]:
            d = distance(l1, l2)
            if d != -1:
                total[0] += d[0]
                total[1] += d[1]

    return [total[0]/n_lines, total[1]/n_lines]


def draw_lines(image, lines, width = 5, color = (0, 0, 255)):

    for x1, y1, x2, y2 in lines[0]:
        cv.line(image, (x1, y1), (x2, y2), color, width)
    return image


def line_count(lines, error = 5):

    total = 0
    v_lines = 0
    h_lines = 0

    for x1, y1, x2, y2 in lines[0]:
        if x1 in range(x2-error, x2+error):
            v_lines += 1
        elif y1 in range(y2-error, y2+error):
            h_lines += 1
        total += 1

    return [total, v_lines, h_lines]


def parallels(line1, line2, error = 5):

    l1_x1, l1_y1, l1_x2, l1_y2 = line1[0]
    l2_x1, l2_y1, l2_x2, l2_y2 = line2[0]

    return (l1_x1 - l2_x1 in range(
        (l1_x2 - l2_x2 - error), (l1_x2 - l2_x2 + error))) \
           and (l1_y1 - l2_y1 in range(
        (l1_y2 - l2_y2 - error), (l1_y2 - l2_y2 + error)))


