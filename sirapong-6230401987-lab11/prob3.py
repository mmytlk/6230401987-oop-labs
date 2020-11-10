import sys
from PyQt5.QtWidgets import *


class Example3(QWidget):
    def __init__(self, parent=None):
        super(Example3, self).__init__(parent)

        label_name = QLabel('Name')
        self.edit_name = QLineEdit()
        fbox = QFormLayout()
        fbox.addRow(label_name, self.edit_name)

        lbox = QHBoxLayout()
        self.b1 = QCheckBox("PyQt")
        self.b1.stateChanged.connect(lambda: self.checkz(self.b1))
        lbox.addWidget(self.b1)

        self.b2 = QCheckBox("PyGame")
        self.b2.toggled.connect(lambda: self.checkz(self.b2))
        lbox.addWidget(self.b2)

        self.b3 = QCheckBox("PyTorch")
        self.b3.toggled.connect(lambda: self.checkz(self.b3))
        lbox.addWidget(self.b3)

        fbox.addRow(QLabel("Library"), lbox)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        self.submit = QPushButton("Submit")
        hbox.addWidget(self.submit)
        self.submit.clicked.connect(lambda :print('Name is ', self.edit_name.text()))
        hbox.addWidget(QPushButton("Cancel"))
        fbox.addRow(hbox)

        self.setLayout(fbox)
        self.setWindowTitle("Problem 3")

    def checkz(self, b):
        if b.isChecked() == True:
            print(b.text() + " is selected")
        else:
            print(b.text() + " is deselected")


def main():
    app = QApplication(sys.argv)
    ex = Example3()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
