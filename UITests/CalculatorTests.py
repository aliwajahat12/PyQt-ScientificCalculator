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
        self.screen.setupUi()
        self.equateButton: QPushButton = self.getButton("=")
        self.addButton: QPushButton = self.getButton("+")
        self.subtractButton: QPushButton = self.getButton("-")
        self.multiplyButton: QPushButton = self.getButton("x")
        self.divideButton: QPushButton = self.getButton("/")
        self.number1Button: QPushButton = self.getButton("1")
        self.number2Button: QPushButton = self.getButton("2")
        self.squareButton: QPushButton = self.getButton("^2")
        self.negateButton: QPushButton = self.getButton("+/-")

    def testAddTwoNumbers(self):
        QTest.mouseClick(self.number1Button, Qt.LeftButton)
        QTest.mouseRelease(self.number1Button, Qt.LeftButton)
        QTest.mouseClick(self.addButton, Qt.LeftButton)
        QTest.mouseRelease(self.addButton, Qt.LeftButton)
        QTest.mouseClick(self.number2Button, Qt.LeftButton)
        QTest.mouseRelease(self.number2Button, Qt.LeftButton)
        QTest.mouseClick(self.equateButton, Qt.LeftButton)
        QTest.mouseRelease(self.equateButton, Qt.LeftButton)
        self.assertEqual(self.screen.answer, "3.0")

    def testSubtractTwoNumbers(self):
        QTest.mouseClick(self.number2Button, Qt.LeftButton)
        QTest.mouseRelease(self.number2Button, Qt.LeftButton)
        QTest.mouseClick(self.subtractButton, Qt.LeftButton)
        QTest.mouseRelease(self.subtractButton, Qt.LeftButton)
        QTest.mouseClick(self.number1Button, Qt.LeftButton)
        QTest.mouseRelease(self.number1Button, Qt.LeftButton)
        QTest.mouseClick(self.equateButton, Qt.LeftButton)
        QTest.mouseRelease(self.equateButton, Qt.LeftButton)
        self.assertEqual(self.screen.answer, "1.0")

    def testMultiplyTwoNumbers(self):
        QTest.mouseClick(self.number1Button, Qt.LeftButton)
        QTest.mouseRelease(self.number1Button, Qt.LeftButton)
        QTest.mouseClick(self.multiplyButton, Qt.LeftButton)
        QTest.mouseRelease(self.multiplyButton, Qt.LeftButton)
        QTest.mouseClick(self.number2Button, Qt.LeftButton)
        QTest.mouseRelease(self.number2Button, Qt.LeftButton)
        QTest.mouseClick(self.equateButton, Qt.LeftButton)
        QTest.mouseRelease(self.equateButton, Qt.LeftButton)
        self.assertEqual(self.screen.answer, "2.0")

    def testDivideTwoNumbers(self):
        QTest.mouseClick(self.number1Button, Qt.LeftButton)
        QTest.mouseRelease(self.number1Button, Qt.LeftButton)
        QTest.mouseClick(self.divideButton, Qt.LeftButton)
        QTest.mouseRelease(self.divideButton, Qt.LeftButton)
        QTest.mouseClick(self.number2Button, Qt.LeftButton)
        QTest.mouseRelease(self.number2Button, Qt.LeftButton)
        QTest.mouseClick(self.equateButton, Qt.LeftButton)
        QTest.mouseRelease(self.equateButton, Qt.LeftButton)
        self.assertEqual(self.screen.answer, "0.5")

    def testSquareNumber(self):
        QTest.mouseClick(self.number2Button, Qt.LeftButton)
        QTest.mouseRelease(self.number2Button, Qt.LeftButton)
        QTest.mouseClick(self.squareButton, Qt.LeftButton)
        QTest.mouseRelease(self.squareButton, Qt.LeftButton)
        self.assertEqual(self.screen.answer, "4.0")

    def testNegateNumber(self):
        QTest.mouseClick(self.number2Button, Qt.LeftButton)
        QTest.mouseRelease(self.number2Button, Qt.LeftButton)
        QTest.mouseClick(self.negateButton, Qt.LeftButton)
        QTest.mouseRelease(self.negateButton, Qt.LeftButton)
        self.assertEqual(self.screen.answer, "-2")

    def tearDown(self) -> None:
        self.screen.deleteLater()

    def getButton(self, text):
        return self.screen.findChild(QPushButton, text)


if __name__ == '__main__':
    unittest.main()
