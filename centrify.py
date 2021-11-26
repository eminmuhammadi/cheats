import sys

from src.centrify import centrify
from drivers.activity import activityListener, looper
from gui.window import Application
import multiprocessing

config = {
    "title" : "Centrify",
    "version" : "0.0.1",
    "button" : "shift"
}

def process():
    return activityListener(config.get("button"), centrify)

"""
Macro
"""
def run():
    looper(process, 0.01)

"""
Main function
"""
def main():
    global config
    Application(run, config)

if __name__ == '__main__':
    try:
        multiprocessing.freeze_support()

        print(f"[+] Starting... hold {config.get('button')} button to activate {config.get('title')} bot")
        main()
    except KeyboardInterrupt:
        sys.exit(0)