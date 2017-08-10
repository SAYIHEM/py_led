from neopixel import *

class Pixel(object):

    ID = None
    STRIP = None

    # Constructor
    def __init__(self, strip, id):
        self.ID = id
        self.STRIP = strip

    # Getter & Setter
    def get_color(self):
        return self.STRIP.getPixelColor(self.ID)

    def __eq__(self, other):
        if isinstance(other, Pixel):
            return self.ID == other.ID
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __str__(self):
        return str(self.ID)
