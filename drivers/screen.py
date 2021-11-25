# https://pyautogui.readthedocs.io/en/latest/  | $ py -m pip install pyautogui
import pyautogui

"""
Returns screen parameters
"""
def screenParameters():
    width, height = pyautogui.size()

    return width, height