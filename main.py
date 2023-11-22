import cv2
import numpy
import matplotlib.pyplot
def modify_image(image):
    grayscaled_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayscaled_image = cv2.GaussianBlur(grayscaled_image, (5, 5), 0)
    gradient_image = cv2.Canny(grayscaled_image, 50, 150)
    return gradient_image
def region_of_interest(image):
    polygon_points = numpy.array([[(300, 700), (500, 580), (700, 570), (1000, 700)]])
    polygon_image = numpy.zeros_like(image)
    cv2.fillPoly(polygon_image, polygon_points, 255)
    return cv2.bitwise_and(image, polygon_image)

def draw_lines(image, lines):
    line_image = image.copy()
    if lines is not None:
        for line in lines:
            fX, fY, sX, sY = line.reshape(4)
            cv2.line(line_image, (fX, fY), (sX, sY), (0, 255, 0), 3)
    return line_image

capture = cv2.VideoCapture('drive_video.mp4')
counter = 0
while capture.isOpened:
    _,principal_frame = capture.read()
    counter = counter + 1
    second_frame = modify_image(principal_frame)
    third_frame = region_of_interest(second_frame)
    lines = cv2.HoughLinesP(third_frame, 1, numpy.pi/180, 18, maxLineGap = 10, minLineLength = 10)
    final_frame = draw_lines(principal_frame, lines)
    cv2.imshow('video', final_frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()


