import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class FormLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.ui()

    def ui(self):
        label_space = QLabel()
        label_simple = QLabel("Simple Form", self)
        label_simple.setStyleSheet('color: blue; font: bold 18px; moving: 50;')


        label_name = QLabel("Name")
        edit_name = QLineEdit()

        fbox = QFormLayout()
        fbox.addRow(label_space, label_simple)
        fbox.addRow(label_name, edit_name)


        hbox = QHBoxLayout()
        radio_male = QRadioButton("Male")
        radio_female = QRadioButton("Female")
        hbox.addWidget(radio_male)
        hbox.addWidget(radio_female)
        hbox.addStretch()
        fbox.addRow(QLabel("Gender"), hbox)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(QPushButton("Submit"))
        hbox.addWidget(QPushButton("Cancel"))
        fbox.addRow(hbox)

        self.setLayout(fbox)
        self.setWindowTitle("Form Layout")
        self.show()


def main():
    app = QApplication(sys.argv)
    form_layouy = FormLayout()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
