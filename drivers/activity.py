# https://pypi.org/project/keyboard/           | py -m pip install keyboard
import keyboard
import time

"""
Listen to function when pressed a button
"""
def activityListener(button, function):
    if keyboard.is_pressed(str(button)):
        function()

"""
Looper
"""
def looper(function, interval):
    while True:
        time.sleep(interval)
        function()
