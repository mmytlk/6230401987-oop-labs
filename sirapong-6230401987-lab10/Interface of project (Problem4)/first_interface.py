from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
import sys


class Engine(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_window()

    def main_window(self):
        background = QtGui.QImage('background.png')
        palette = QtGui.QPalette()
        palette.setBrush(10, QtGui.QBrush(background))

        btn_start = QPushButton('START', self)
        btn_start.setFont(QFont('Eras Bold ITC'))
        btn_start.setGeometry(350, 650, 200, 50)
        btn_start.setStyleSheet('QPushButton{background-color: rgb(22, 23, 25);border-style: '
                                'outset;border-width: 2px;border-radius: '
                                '10px;border-color: red;font: bold 14px;'
                                'color: red;min-width: 10em;padding: 6px;}'
                                'QPushButton::pressed{background-color: white;}')

        btn_quit = QPushButton('QUIT', self)
        btn_quit.setFont(QFont('Eras Bold ITC'))
        btn_quit.setGeometry(670, 650, 200, 50)
        btn_quit.setStyleSheet('QPushButton{background-color: rgb(22, 23, 25);border-style: '
                               'outset;border-width: 2px;border-radius: '
                               '10px;border-color: red;font: bold 14px;'
                               'color: red;min-width: 10em;padding: 6px;}'
                               'QPushButton::pressed{background-color: white;}')
        btn_quit.clicked.connect(QApplication.instance().quit)

        pic = QLabel(self)
        pixmap = QPixmap()
        pic.setPixmap(pixmap)
        pic.setScaledContents(True)
        pic.resize(200, 200)
        pic.move(600, 400)

        self.setPalette(palette)
        self.resize(1200, 800)
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.setWindowTitle('TYPE GAME')
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


def main_run():
    app = QApplication(sys.argv)
    run = Engine()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main_run()
