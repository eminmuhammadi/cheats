import time

from drivers.screen import screenParameters
from drivers.mouse import moveTo

"""
Forcely center the mouse cursor on the screen.
"""
def centrify():
    time.sleep(0.01)

    # Get the screen parameters
    width, height = screenParameters()

    time.sleep(0.05)

    X = int(width)  / 2
    Y = int(height) / 2

    moveTo(X, Y)
