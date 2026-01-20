import sys
import ctypes
from display import LineEdit, Info, ButtonsGrid
from PySide6.QtGui import QIcon
from variables import FILE_ICON
from main_window import MainWindow
from PySide6.QtWidgets import QApplication
from styles import setupTheme

if __name__ == "__main__":

    # ESSENCIAL NO WINDOWS (taskbar)
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        "calculadora.python.pyside6"
    )

    # Creation
    app = QApplication(sys.argv)
    setupTheme(app)

    # Icon
    icon = QIcon(str(FILE_ICON))
    app.setWindowIcon(icon)

    window = MainWindow()
    window.setWindowIcon(icon)

    # Information bar
    info = Info(" ")
    window.addToVLayout(info)

    # Input bar
    display = LineEdit()
    window.addToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    window.adjustFixedsize()
    window.show()
    app.exec()
