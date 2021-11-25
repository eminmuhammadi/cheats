import time

from drivers.mouse import boundingBoxCenter, click, moveTo
from drivers.rgb import rgbPixelScreenShot

"""
Trigger if the pixels are different
"""
def trigger():
    time.sleep(0.01)

    # Get the current mouse position with the bounding box
    X1, Y1, X2, Y2 = boundingBoxCenter()

    # Get the RGB values of the pixel
    pixel = rgbPixelScreenShot(X1, Y1, X2, Y2)

    # Sleep
    time.sleep(0.05)

    # New rgb values
    newPixel = rgbPixelScreenShot(X1, Y1, X2, Y2)

    # Calculate the difference
    if abs(pixel - newPixel) > 5:
        click()