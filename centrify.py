import sys

from src.centrify import centrify
from drivers.activity import activityListener, looper

_BUTTON_ = "shift"

def process():
    return activityListener(_BUTTON_, centrify)

"""
Macro
"""
def main():
    looper(process, 0.01)

if __name__ == '__main__':
    try:
        print(f"[+] Starting... hold {_BUTTON_} button to activate centrify bot")
        main()
    except KeyboardInterrupt:
        sys.exit(0)
