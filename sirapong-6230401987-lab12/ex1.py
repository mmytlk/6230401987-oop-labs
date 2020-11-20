from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_value = 50
        self.button = None
        self.rem = None
        self.num1 = 50
        self.num2 = 50

        self.ui()

    def main_slider(self):
        slider = QSlider(Qt.Horizontal, self)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(50)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(5)
        return slider

    def main_label(self):
        label = QLabel(self)
        label.setText(str(self.init_value))
        label.setFont(QFont('Arial', 20))
        label.setStyleSheet('color: blue')
        return label

    def ui(self):
        flayer = QFormLayout()

        g1 = QGridLayout()
        self.slider1 = self.main_slider()
        self.slider1.valueChanged[int].connect(self.change_value1)
        self.label1 = self.main_label()
        self.slider2 = self.main_slider()
        self.slider2.valueChanged[int].connect(self.change_value2)
        self.label2 = self.main_label()

        g1.addWidget(self.label1, 0, 0)
        g1.addWidget(self.slider1, 0, 1)
        g1.addWidget(self.label2, 1, 0)
        g1.addWidget(self.slider2, 1, 1)
        flayer.addRow(g1)

        g2 = QGridLayout()
        self.add = QPushButton('Add', self)
        self.add.clicked.connect(self.color)
        self.sub = QPushButton('Subtract', self)
        self.sub.clicked.connect(self.color)
        self.mul = QPushButton('Multiply', self)
        self.mul.clicked.connect(self.color)
        self.div = QPushButton('Divide', self)
        self.div.clicked.connect(self.color)

        g2.addWidget(self.add, 3, 0)
        g2.addWidget(self.sub, 3, 1)
        g2.addWidget(self.mul, 3, 2)
        g2.addWidget(self.div, 3, 3)
        flayer.addRow(g2)

        g3 = QGridLayout()
        name = QLabel('Result', self)
        name.setFont(QFont('Arial', 10))
        self.edit_line = QLineEdit(self)
        self.edit_line.setDisabled(True)
        self.edit_line.setFont(QFont('Arial', 25))
        self.edit_line.setStyleSheet('background-color: gray;'
                                     'color: yellow;')
        self.edit_line.setAlignment(Qt.AlignRight)

        g3.addWidget(name, 4, 0)
        g3.addWidget(self.edit_line, 4, 1)
        flayer.addRow(g3)

        self.setLayout(flayer)
        self.adjustSize()
        self.setWindowTitle('Simple Calculator')
        self.show()

    def cal(self):
        if self.button == 'click':
            op = self.sen.text()
            if op == "Add":
                cal = self.num1 + self.num2
            elif op == "Subtract":
                cal = self.num1 - self.num2
            elif op == "Multiply":
                cal = self.num1 * self.num2
            elif op == "Divide":
                try:
                    cal = self.num1 / self.num2
                except ZeroDivisionError:
                    cal = 'Not Valid'
            else:
                cal = ""
            self.edit_line.setText(str(cal))

        else:
            pass

    def color(self):
        self.sen = self.sender()
        if self.sen:
            self.button = "click"
            if self.rem == None:
                self.sen.setStyleSheet('background-color: green')
                self.rem = self.sen
            else:
                self.sen.setStyleSheet('background-color: green')
                self.rem.setStyleSheet('background-color: None')
                self.rem = self.sen
        else:
            pass

    def change_value1(self, value):
        updated_value = value
        self.num1 = value
        self.cal()
        self.label1.setText(str(updated_value))

    def change_value2(self, value):
        updated_value = value
        self.num2 = value
        self.cal()
        self.label2.setText(str(updated_value))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
