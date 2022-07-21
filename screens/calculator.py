from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget


def convert_str_to_num(text):
    if text[0] == "-":
        num = float(text[1:])
        return -1 * num
    else:
        return float(text)


class Calculator(QWidget):

    def __init__(self):
        super(Calculator, self).__init__()
        self.design_layout = QVBoxLayout(self)
        self.answer = "0"
        self.previous_number = "0"
        self.operation = None
        self.number1 = None
        self.number2 = None
        self.number3 = None
        self.number4 = None
        self.number5 = None
        self.number6 = None
        self.number7 = None
        self.number8 = None
        self.number9 = None
        self.number0 = None
        self.add_button = None
        self.subtract_button = None
        self.multiply_button = None
        self.divide_button = None
        self.equals_button = None
        self.reset_button = None
        self.negate_button = None
        self.decimal_button = None
        self.square_button = None
        self.exponent_button = None
        self.backspace_button = None
        self.answerLabel = None
        self.isNegate = False
        self.setGeometry(500, 100, 500, 300)
        self.setWindowTitle("Scientific Calculator")

    def number_pressed(self, num):
        if self.answer == "0":
            self.answer = ""
        self.answer = self.answer + num
        self.update_answer()

    def reset(self, text):
        self.answer = "0"
        self.previous_number = "0"
        self.operation = None
        self.update_answer()

    def squared(self, text):
        num = float(self.answer)
        num = num * num
        self.answer = str(num)
        self.update_answer()

    def get_previous_number(self):
        self.previous_number = self.answer
        if self.isNegate:
            self.isNegate = False

    def add(self, text):
        if self.operation is None:
            self.get_previous_number()
        else:
            self.equate("")
        if self.answerLabel.text() != "Invalid Operation":
            self.operation = "+"
            self.answer = self.answer + "+"
            self.update_answer()

    def subtract(self, text):
        if self.operation is None:
            self.get_previous_number()
        else:
            self.equate("")
        if self.answerLabel.text() != "Invalid Operation":
            self.operation = "-"
            self.answer = self.answer + "-"
            self.update_answer()

    def multiply(self, text):
        if self.operation is None:
            self.get_previous_number()
        else:
            self.equate("")
        if self.answerLabel.text() != "Invalid Operation":
            self.operation = "*"
            self.answer = self.answer + "x"
            self.update_answer()

    def divide(self, text):
        if self.operation is None:
            self.get_previous_number()
        else:
            self.equate("")
        if self.answerLabel.text() != "Invalid Operation":
            self.operation = "/"
            self.answer = self.answer + "/"
            self.update_answer()

    def negate(self, text):
        self.isNegate = not self.isNegate
        if self.isNegate:
            if self.previous_number == "0":
                self.answer = "-" + self.answer
            else:
                self.answer = self.answer[:len(self.previous_number) + 1] + "-" + self.answer[
                                                                                  len(self.previous_number) + 1:]
            self.update_answer()
        else:
            if self.previous_number == "0":
                self.answer = self.answer[1:]
            else:
                self.answer = self.answer[:len(self.previous_number) + 1] + self.answer[
                                                                            len(self.previous_number) + 2:]
            self.update_answer()

    def equate(self, text):
        try:
            second_arg = self.answer[len(self.previous_number) + 1:]
            if not any(char.isdigit() for char in second_arg):
                raise ValueError('err')
            else:
                if self.operation == "+":
                    self.answer = str(convert_str_to_num(self.previous_number) + convert_str_to_num(second_arg))
                elif self.operation == "-":
                    self.answer = str(convert_str_to_num(self.previous_number) - convert_str_to_num(second_arg))
                elif self.operation == "*":
                    self.answer = str(convert_str_to_num(self.previous_number) * convert_str_to_num(second_arg))
                elif self.operation == "/":
                    self.answer = str(convert_str_to_num(self.previous_number) / convert_str_to_num(second_arg))

                self.previous_number = self.answer
                self.operation = None
                self.update_answer()
        except Exception as e:
            self.invalid_operation()

    def backspace(self, text):
        self.answer = self.answer[:-1]
        if self.answer == "":
            self.answer = "0"
        self.update_answer()

    def update_answer(self):
        self.answerLabel.setText(self.answer)
        self.answerLabel.adjustSize()

    def invalid_operation(self):
        self.answerLabel.setText("Invalid Operation")
        self.previous_number = "0"
        self.answer = "0"
        self.operation = None
        self.answerLabel.adjustSize()

    def setupButton(self, text, func):
        button_variable = QPushButton(text, parent=self)
        button_variable.clicked.connect(lambda: func(text))
        button_variable.setObjectName(text)
        return button_variable

    def setupUi(self):
        answer_row = QHBoxLayout()

        self.answerLabel = QLabel(self.answer, parent=self)
        answer_row.addWidget(self.answerLabel)

        row0 = QHBoxLayout()

        self.square_button = self.setupButton("^2", self.squared)
        self.exponent_button = self.setupButton("/", self.divide)
        self.reset_button = self.setupButton("C", self.reset)
        self.backspace_button = self.setupButton("<-", self.backspace)

        row0.addWidget(self.square_button, 3)
        row0.addWidget(self.exponent_button, 3)
        row0.addWidget(self.reset_button, 3)
        row0.addWidget(self.backspace_button, 3)

        row1 = QHBoxLayout()

        self.number1 = self.setupButton("1", self.number_pressed)
        self.number2 = self.setupButton("2", self.number_pressed)
        self.number3 = self.setupButton("3", self.number_pressed)
        self.add_button = self.setupButton("+", self.add)

        row1.addWidget(self.number1, 3)
        row1.addWidget(self.number2, 3)
        row1.addWidget(self.number3, 3)
        row1.addWidget(self.add_button, 3)

        row2 = QHBoxLayout()

        self.number4 = self.setupButton("4", self.number_pressed)
        self.number5 = self.setupButton("5", self.number_pressed)
        self.number6 = self.setupButton("6", self.number_pressed)
        self.subtract_button = self.setupButton("-", self.subtract)

        row2.addWidget(self.number4, 3)
        row2.addWidget(self.number5, 3)
        row2.addWidget(self.number6, 3)
        row2.addWidget(self.subtract_button, 3)

        row3 = QHBoxLayout()

        self.number7 = self.setupButton("7", self.number_pressed)
        self.number8 = self.setupButton("8", self.number_pressed)
        self.number9 = self.setupButton("9", self.number_pressed)
        self.multiply_button = self.setupButton("x", self.multiply)

        row3.addWidget(self.number7, 3)
        row3.addWidget(self.number8, 3)
        row3.addWidget(self.number9, 3)
        row3.addWidget(self.multiply_button, 3)

        row4 = QHBoxLayout()

        self.negate_button = self.setupButton("+/-", self.negate)
        self.number0 = self.setupButton("0", self.number_pressed)
        self.decimal_button = self.setupButton(".", self.number_pressed)
        self.equals_button = self.setupButton("=", self.equate)

        row4.addWidget(self.negate_button, 3)
        row4.addWidget(self.number0, 3)
        row4.addWidget(self.decimal_button, 3)
        row4.addWidget(self.equals_button, 3)

        self.design_layout.addLayout(answer_row)
        self.design_layout.addLayout(row0)
        self.design_layout.addLayout(row1)
        self.design_layout.addLayout(row2)
        self.design_layout.addLayout(row3)
        self.design_layout.addLayout(row4)

        self.setLayout(self.design_layout)
