import sys
from functools import partial
from PyQt5.QtWidgets import QApplication, QGridLayout, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget

MSG='ERROR OCCURED'

class CalcView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Calculator")
        self.setFixedSize(300, 300)
        self.generalLayout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.generalLayout)
        self.Display()
        self.dispalyButtons()

    def Display(self):

        self.display = QLineEdit()
        self.display.setFixedHeight(40)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def dispalyButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        buttons = {"7": (0, 0), "8": (0, 1), "9": (0, 2), "/": (0, 3), "c": (0, 4),
            "4": (1, 0), "5": (1, 1), "6": (1, 2), "*": (1, 3), "(": (1, 4),
            "1": (2, 0), "2": (2, 1), "3": (2, 2), "-": (2, 3), ")": (2, 4),
            "0": (3, 0), "00": (3, 1), ".": (3, 2), "+": (3, 3), "=": (3, 4)
        }

        for buttonText, position in buttons.items():
            self.buttons[buttonText] = QPushButton(buttonText)
            self.buttons[buttonText].setFixedSize(45, 45)
            buttonsLayout.addWidget(self.buttons[buttonText], position[0], position[1])
        self.generalLayout.addLayout(buttonsLayout)

    def setTextToDisplay(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def getTextToDisplay(self):
        return self.display.text()

    def clearTheScreen(self):
        self.setTextToDisplay("")


def CalcModel(equation):
    try:
        result = str(eval(equation, {}, {}))
    except:
        result = MSG

    return result


class CalcController():
    def __init__(self, model, view):
        self.evaluate = model
        self.view = view
        self.SignalsAndSlots()

    def calculate(self):
        result = self.evaluate(equation=self.view.getTextToDisplay())
        self.view.setTextToDisplay(result)

    def setExpression(self, sub_exp):
        if self.view.getTextToDisplay() == MSG:
            self.view.clearTheScreen()

        self.view.setTextToDisplay(self.view.getTextToDisplay() + sub_exp)

    def SignalsAndSlots(self):
        for bottonText, botton in self.view.buttons.items():
            if bottonText not in {"=", "C"}:
                botton.clicked.connect(partial(self.setExpression, bottonText))

        self.view.buttons["="].clicked.connect(self.calculate)
        self.view.display.returnPressed.connect(self.calculate)
        self.view.buttons["c"].clicked.connect(self.view.clearTheScreen)


def main():
    Calc = QApplication(sys.argv)
    view = CalcView()
    view.show()
    model = CalcModel
    CalcController(model=model, view=view)
    sys.exit(Calc.exec_())


if __name__ == "__main__":
    main()