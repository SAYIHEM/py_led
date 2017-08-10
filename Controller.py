import neopixel
import rpi_ws281x as ws
from Pixel import *
from PixelGroup import *

class Controller(object):

    # LED strip configuration:
    LED_COUNT = 194  # Number of LED pixels.
    LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
    # LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
    LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA = 5  # DMA channel to use for generating signal (try 5)
    LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
    LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
    LED_STRIP = ws.WS2812_STRIP  # Strip type and colour ordering

    # Var for strip instance
    STRIP = None

    # Pixel array
    PIXELS = []

    # Constructor
    def __init__(self, numberLED):
        # Set count of LEDs
        self.LED_COUNT = numberLED

        # Initialize strip object
        self.STRIP = Adafruit_NeoPixel(self.LED_COUNT,
                                       self.LED_PIN,
                                       self.LED_FREQ_HZ,
                                       self.LED_DMA,
                                       self.LED_INVERT,
                                       self.LED_BRIGHTNESS,
                                       self.LED_CHANNEL,
                                       self.LED_STRIP)

        # Initialize pixel list
        for i in range(self.LED_COUNT):
            self.PIXELS.append(Pixel(self.STRIP, i))

        # Start LED control
        self.STRIP.begin()

        group = PixelGroup(self.STRIP, [Pixel(None, 1), Pixel(None, 2)])
        group.add_pixel(Pixel(None, 5))
        group.delete_pixel(Pixel(None, 1))
        print(group.PIXEL_GROUP)



    # Getter & Setter #
    def pixel_count(self):
        return self.LED_COUNT

    def change_brightness(self, pixel, value):
        # Get old pixel color
        color = self.STRIP.getPixelColor(pixel)
        # Set new lowlighted colors
        for i in range(2):
            if (color[i] + value) < 0:
                color[i] = 0
            elif (color[i] + value) > 255:
                color[i] = 255
            else:
                color[i] = color[i] + value
        self.STRIP.setPixelColorRGB(pixel, color)

    def set_pixel(self, pixel, r, g, b):
        self.STRIP.setPixelColorRGB(pixel, r, g, b)

    def show(self):
        self.STRIP.show()
