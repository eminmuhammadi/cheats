# https://pypi.org/project/d3dshot/ | $ py -m pip install d3dshot
import d3dshot as d3d

# https://numpy.org/install/        | $ py -m pip install numpy
import numpy as np

d3dshot = d3d.create(capture_output="numpy")

"""
rgbPixelScreenShot

Take a screenshot of the screen and return the 
average RGB values of the specified region.
"""
def rgbPixelScreenShot(X1, Y1, X2, Y2):
    return np.average(d3dshot.screenshot(region=(X1, Y1, X2, Y2)))