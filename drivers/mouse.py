# https://pyautogui.readthedocs.io/en/latest/  | $ py -m pip install pyautogui
import pyautogui

from drivers.screen import screenParameters

_BOX_LENGTH_ = int(4)

"""
Boundary box on center of screen
"""
def boundingBoxCenter():
    ## Current screen resolution
    width, height = screenParameters()

    X = int(width)  / 2
    Y = int(height) / 2
    error = _BOX_LENGTH_ / 2

    ## X axis
    X1 = int(X  - error)
    X2 = int(X  + error)

    ## Y axis
    Y1 = int(Y  - error)
    Y2 = int(Y  + error)

    return X1, Y1, X2, Y2

"""
Mouse Click
"""
def click():
    return pyautogui.click()

"""
Move mouse to X and Y coordinates
"""
def moveTo(x, y):
    return pyautogui.moveTo(x, y)