from neopixel import *
from Pixel import *


class PixelGroup(object):

    PIXEL_GROUP = []
    STRIP = None

    # Constructor
    def __init__(self, strip, pixel_group):
        self.PIXEL_GROUP = pixel_group
        self.STRIP = strip



    # Getter & Setter

    def add_pixel(self, pixel):
        self.PIXEL_GROUP.append(pixel)

    def delete_pixel(self, id):
        try:
            self.PIXEL_GROUP.remove(Pixel(None, id))
        except ValueError:
            pass
            return False
        return True
