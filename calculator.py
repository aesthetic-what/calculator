import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculator.ui", self)

        self.act1.clicked.connect(self.action1)
        self.act2.clicked.connect(self.action2)
        self.act3.clicked.connect(self.action3)
        self.act4.clicked.connect(self.action4)
        self.act5.clicked.connect(self.action5)
        self.act6.clicked.connect(self.action6)
        self.act7.clicked.connect(self.action7)
        self.act8.clicked.connect(self.action8)
        self.act9.clicked.connect(self.action9)
        self.act0.clicked.connect(self.action0)

        self.actplus.clicked.connect(self.event_plus)
        self.actminus.clicked.connect(self.event_minus)
        self.actmul.clicked.connect(self.event_mul)
        self.actdiv.clicked.connect(self.event_div)
        self.actdel.clicked.connect(self.event_clear)
        self.acteqal.clicked.connect(self.event_equal)

        self.hamster.clicked.connect(self.hamster_button)

    def event_equal(self):
        equation = self.label.text()
        try:
            ans = eval(equation)

            self.label.setText(str(ans))
        except:
            self.label.setText("ошибка")

    def event_plus(self):
        text = self.label.text()
        self.label.setText(text + " + ")

    def event_minus(self):
        text = self.label.text()
        self.label.setText(text + " - ")

    def event_mul(self):
        text = self.label.text()
        self.label.setText(text + " * ")

    def event_div(self):
        text = self.label.text()
        self.label.setText(text + " / ")

    def event_point(self):
        text = self.label.text()
        self.label.setText(text + " . ")

    def action1(self):
        text = self.label.text()
        self.label.setText(text + "1")

    def action2(self):
        text = self.label.text()
        self.label.setText(text + "2")

    def action3(self):
        text = self.label.text()
        self.label.setText(text + "3")

    def action4(self):
        text = self.label.text()
        self.label.setText(text + "4")

    def action5(self):
        text = self.label.text()
        self.label.setText(text + "5")

    def action6(self):
        text = self.label.text()
        self.label.setText(text + "6")

    def action7(self):
        text = self.label.text()
        self.label.setText(text + "7")

    def action8(self):

        text = self.label.text()
        self.label.setText(text + "8")

    def action9(self):
        text = self.label.text()
        self.label.setText(text + "9")

    def action0(self):
        text = self.label.text()
        self.label.setText(text + "0")

    def event_clear(self):
        self.label.setText("")

    def hamster_button(self):
        os.system(r'python C:\Users\ZV\caculator\hamster_combat.py')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main_window()
    window.show()
    sys.exit(app.exec_())
