import sys
from PyQt5.QtWidgets import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.ui()

    def ui(self):
        btn = QPushButton('Quit', self)
        btn.clicked.connect(QApplication.instance().quit)
        btn.setToolTip('Click to exit')
        btn.resize(btn.sizeHint())
        btn.move(110, 100)
        label = QLabel(f'My name is {sys.argv[1]}', self)
        label.move(100, 80)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Exercise 1')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     'Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication([sys.argv])
    exam = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
