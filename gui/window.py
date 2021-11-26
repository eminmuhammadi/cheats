import sys
import os
from multiprocessing import Process

from PyQt6.QtWidgets import (
    QWidget      as Widget, 
    QPushButton  as PushButton,
    QApplication as App,
    QMessageBox  as MessageBox,
)

"""
Container
"""
class Window(Widget):

    def __init__(self, func, config):
        super().__init__()
        
        self.func    = func
        self.config  = config
        self.pressed = False
        self.process = Process(target=self.func)
        self.initUI()

    """
    Initialize the UI
    """
    def initUI(self):
        #
        # Application
        #
        self.setWindowTitle(f"{self.config.get('title')}::{self.config.get('version')}")
        self.resize(270, 50)
        self.setContentsMargins(0, 20, 0, 0)
        self.center()

        #
        # Button
        #
        startButton = PushButton('Start', self)
        startButton.setGeometry(10, 10, 250, 30)
        startButton.clicked[bool].connect(self.run)

        #
        # Start
        #
        self.show()

    """
    Run the function
    """
    def run(self, pressed):
        if pressed != True:
            self.process.start()

    """
    Quit alert
    """
    def closeEvent(self, event):
        reply = MessageBox.question(
                self, 
                'Alert',
                "Are you sure to quit?",
                MessageBox.StandardButton.Yes | MessageBox.StandardButton.No, 
                MessageBox.StandardButton.No
            )

        if reply == MessageBox.StandardButton.Yes:
            if self.pressed:
                self.process.terminate()
            event.accept()
        else:
            event.ignore()
    
    """
    Center the window
    """
    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())


def Application(func, config):
    app       = App(sys.argv)
    container = Window(func, config)

    # Run the app
    sys.exit(app.exec())