import sys

from src.trigger import trigger
from drivers.activity import activityListener, looper
from gui.window import Application
import multiprocessing

config = {
    "title" : "Trigger",
    "version" : "0.0.1",
    "button" : "alt"
}

def process():
    return activityListener(config.get("button"), trigger)

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
    multiprocessing.freeze_support()

    try:
        print(f"[+] Starting... hold {config.get('button')} button to activate {config.get('title')} bot")
        main()
    except KeyboardInterrupt:
        sys.exit(0)
