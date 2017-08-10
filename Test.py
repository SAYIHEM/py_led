import time

from neopixel import *
import rpi_ws281x as ws


# LED strip configuration:
from Controller import *

LED_COUNT = 194  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5  # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP = ws.WS2812_STRIP  # Strip type and colour ordering


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, wheel((i + j) % 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)

def ping_pong(strip):
    for j in range(256):
        for q in range(5):
            for i in range(0, strip.numPixels(), 10):
                strip.setPixelColor(i + q, 100)
            strip.show()
            time.sleep(1000.0)
    for a in range(0, strip.numPixels(), 1):
        strip.setPixelColor(a, 1)

def lowlight(strip):
    clear_pixels(strip)
    for b in range(1, 255, 25):
        for i in range(0, strip.numPixels(), 1):
            strip.setPixelColorRGB(i, b, b, b)
            strip.show()
            time.sleep(0.005)

def shoot(strip, iterations = 3):
    clear_pixels(strip)
    for n in range(1, iterations, 1):
        for i in range(0, strip.numPixels(), 2):
            strip.setPixelColorRGB(i, 255, 255, 0)
            if i >= 1:
                strip.setPixelColorRGB(i - 1, 212, 212, 0)
            if i >= 2:
                strip.setPixelColorRGB(i - 2, 170, 170, 0)
            if i >= 3:
                strip.setPixelColorRGB(i - 3, 127, 127, 0)
            if i >= 4:
                strip.setPixelColorRGB(i - 4, 85, 85, 0)
            if i >= 5:
                strip.setPixelColorRGB(i - 5, 42, 42, 0)
            if i >= 6:
                strip.setPixelColorRGB(i - 6, 0, 0, 0)
            if i >= 7:
                strip.setPixelColorRGB(i - 7, 0, 0, 0)
            strip.show()

def clear_pixels(strip):
    for i in range(0, strip.numPixels(), 1):
        strip.setPixelColorRGB(i, 0, 0, 0)
    strip.show()



#if __name__ == '__main__':
# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL,
                          LED_STRIP)
# Intialize the library (must be called once before other functions).
strip.begin()
shoot(strip, 5000)


