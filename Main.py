from Controller import *
import colorsys
from neopixel import *
from PixelGroup import *

import time


controller = Controller(194)


# for i in range(controller.pixel_count()):
#     controller.set_pixel(i, 255, 255, 255)
#     controller.STRIP.show()
#
# time.sleep(0.5)
#
# for i in range(97):
#     for k in range(controller.pixel_count()):
#         controller.set_pixel(k, 255, 255, 255)
#     controller.STRIP.show()
#     for k in range(controller.pixel_count()):
#         controller.set_pixel(k, 0, 0, 0)
#     controller.STRIP.show()



def swipe_thru_every_color():
    for b in range(0, 255):
        for g in range(0, 255):
            for r in range(0, 255):
                for p in range(194):
                    controller.setPixelRGB(p, r, g, b)
                controller.show()
                time.sleep(0.05)


def swipe_smooth():
    while True:
        for j in range(0, 720*5):
            clr = colorsys.hsv_to_rgb(j / 720.0*5, 1, 1)
            for p in range(194):
                controller.setPixelRGB(p, int(clr[0]*255), int(clr[1]*255), int(clr[2]*255))
            controller.show()


def swipe_smooth_rainbow(start, end):
    k = 0

    colors = []
    for j in range(0, 194):
        colors.append(colorsys.hsv_to_rgb(abs(start + end - 1.0)/194.0 * j + start, 1, 1))

    while True:
        k += 1
        for y in range(0, 194):
            index = (y + k) % 194
            controller.setPixelRGB(index, int(colors[y][0] * 255), int(colors[y][1] * 255), int(colors[y][2] * 255))
        controller.show()
        time.sleep(0.05)


#swipe_thru_every_color()
swipe_smooth_rainbow(0.01, 0.6)
#swipe_smooth()
#time.sleep(5)
while True:
    for i in range(200):
        for p in range(194):
            controller.setPixelRGB(p, 200, i, 0)
        controller.show()
        time.sleep(0.03)
    for i in range(200):
        for p in range(194):
            controller.setPixelRGB(p, 200 - i, 200, 0)
        controller.show()
        time.sleep(0.03)
    for i in range(200):
        for p in range(194):
            controller.setPixelRGB(p, 0, 200, i)
        controller.show()
        time.sleep(0.03)
    for i in range(200):
        for p in range(194):
            controller.setPixelRGB(p, 0, 200 - i, 200)
        controller.show()
        time.sleep(0.03)
    for i in range(200):
        for p in range(194):
            controller.setPixelRGB(p, i, 0, 200)
        controller.show()
        time.sleep(0.03)
    for i in range(200):
        for p in range(194):
            controller.setPixelRGB(p, 200, 0, 200 - i)
        controller.show()
        time.sleep(0.03)

