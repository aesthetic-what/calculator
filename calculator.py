import math
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculator.ui", self)

        self.angle_mode = "degrees"

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
        self.acteqal.clicked.connect(self.event_equal)
        self.pl_min.clicked.connect(self.plus_minus)
        self.proc.clicked.connect(self.procent)
        self.actpoint.clicked.connect(self.event_point)

        self.rightbr.clicked.connect(self.event_right_bracket)
        self.leftbr.clicked.connect(self.event_left_bracket)

        self.actsin.clicked.connect(self.event_sin)
        self.actcos.clicked.connect(self.event_cos)
        self.actlog.clicked.connect(self.event_log)
        self.actln.clicked.connect(self.event_ln)

        self.actdel.clicked.connect(self.event_clear)
        self.delall.clicked.connect(self.event_clear_all)

    def event_equal(self):
        equation = self.label.text()
        equation = equation.replace("%", "/100")
        try:
            # Переопределяем eval для поддержки математических функций
            ans = eval(equation, {
                "sin": lambda x: math.sin(math.radians(x)),
                "cos": lambda x: math.cos(math.radians(x)),
                "log": math.log10,
                "ln": math.log,
            })
            self.label.setText(str(ans))
        except:
            self.label.setText("ошибка")

    def event_plus(self):
        self.label.setText(self.label.text() + " + ")

    def event_minus(self):
        self.label.setText(self.label.text() + " - ")

    def event_mul(self):
        self.label.setText(self.label.text() + " * ")

    def event_div(self):
        self.label.setText(self.label.text() + " / ")

    def event_sin(self):
        self.label.setText(self.label.text() + "sin(")

    def event_cos(self):
        self.label.setText(self.label.text() + "cos(")

    def event_log(self):
        self.label.setText(self.label.text() + "log(")

    def event_ln(self):
        self.label.setText(self.label.text() + "ln(")

    def event_left_bracket(self):
        self.label.setText(self.label.text() + "(")

    def event_right_bracket(self):
        self.label.setText(self.label.text() + ")")

    def event_point(self):
        text = self.label.text()
        try:
            if self.label.text()[-1] == ".":
                pass
            else:
                self.label.setText(f'{text}.')
        except IndexError:
            self.label.setText("Ошибка")

    def procent(self):
        self.label.setText(self.label.text() + "%")

    def action1(self):
        self.label.setText(self.label.text() + "1")

    def action2(self):
        self.label.setText(self.label.text() + "2")

    def action3(self):
        self.label.setText(self.label.text() + "3")

    def action4(self):
        self.label.setText(self.label.text() + "4")

    def action5(self):
        self.label.setText(self.label.text() + "5")

    def action6(self):
        self.label.setText(self.label.text() + "6")

    def action7(self):
        self.label.setText(self.label.text() + "7")

    def action8(self):
        self.label.setText(self.label.text() + "8")

    def action9(self):
        self.label.setText(self.label.text() + "9")

    def action0(self):
        self.label.setText(self.label.text() + "0")

    def event_clear(self):
        self.label.setText(self.label.text()[:-1])

    def event_clear_all(self):
        self.label.setText("")

    # Изменение с положительного / отрицательного
    def plus_minus(self):
        screen = self.label.text()
        if "-" in screen:
            self.label.setText(screen.replace("-", ""))
        else:
            self.label.setText(f'-{screen}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main_window()
    window.show()
    sys.exit(app.exec_())
