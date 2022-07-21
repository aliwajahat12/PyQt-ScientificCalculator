import sys
import unittest

from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest

from screens.calculator import Calculator

app = QApplication(sys.argv)


class CalculatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.screen: Calculator = Calculator()
        self.equateButton: QPushButton = self.getButton("=")
        self.addButton: QPushButton = self.getButton("+")
        self.subtractButton: QPushButton = self.getButton("-")
        self.multiplyButton: QPushButton = self.getButton("*")
        self.divideButton: QPushButton = self.getButton("/")
        self.number1Button: QPushButton = self.getButton("1")
        self.number2Button: QPushButton = self.getButton("2")

    def testAddTwoNumbers(self):
        QTest.mouseClick(self.number1Button, Qt.LeftButton)
        QTest.mouseRelease(self.number1Button, Qt.LeftButton)
        QTest.mouseClick(self.addButton, Qt.LeftButton)
        QTest.mouseRelease(self.addButton, Qt.LeftButton)
        QTest.mouseClick(self.number2Button, Qt.LeftButton)
        QTest.mouseRelease(self.number2Button, Qt.LeftButton)
        self.assertEqual(self.screen.answer, "3.0")

    def tearDown(self) -> None:
        self.screen.deleteLater()

    def getButton(self, text):
        return self.screen.findChild(QPushButton, text)
