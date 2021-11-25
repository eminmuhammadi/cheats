import sys

from src.trigger import trigger
from drivers.activity import activityListener, looper

_BUTTON_ = "alt"

def process():
    return activityListener(_BUTTON_, trigger)

"""
Macro
"""
def main():
    looper(process, 0.01)

if __name__ == '__main__':
    try:
        print(f"[+] Starting... hold {_BUTTON_} button to activate trigger bot")
        main()
    except KeyboardInterrupt:
        sys.exit(0)
