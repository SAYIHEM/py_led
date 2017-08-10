from Controller import *
from neopixel import *
from PixelGroup import *

import time


controller = Controller(194)


for i in range(controller.pixel_count()):
    controller.set_pixel(i, 255, 255, 255)
    controller.STRIP.show()

time.sleep(0.5)

for i in range(97):
    for k in range(controller.pixel_count()):
        controller.set_pixel(k, 255, 255, 255)
    controller.STRIP.show()
    for k in range(controller.pixel_count()):
        controller.set_pixel(k, 0, 0, 0)
    controller.STRIP.show()
