import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton

from screens.calculator import Calculator

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.setupUi()
    window.show()
    app.exec()
