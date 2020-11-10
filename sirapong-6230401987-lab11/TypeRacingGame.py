from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class StartWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window()

    def main_window(self):
        background = QImage('bg_first.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(background))

        btn_start = QPushButton('START', self)
        btn_start.setFont(QFont('Eras Bold ITC'))
        btn_start.setGeometry(350, 650, 200, 50)
        btn_start.setStyleSheet('QPushButton{background-color: rgb(22, 23, 25);border-style: '
                                'outset;border-width: 2px;border-radius: '
                                '10px;border-color: red;font: bold 14px;'
                                'color: red;min-width: 10em;padding: 6px;}'
                                'QPushButton::pressed{background-color: white;}')
        btn_start.clicked.connect(self.next_guest_input)

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
        pixmap = QPixmap('logo.png')
        pic.setPixmap(pixmap)
        pic.setScaledContents(True)
        pic.resize(100, 100)
        pic.move(560, 500)

        self.setPalette(palette)
        self.resize(1200, 800)
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle('TYPE GAME')
        self.show()

    @pyqtSlot()
    def next_guest_input(self):
        self.openz = GuestInput()
        self.openz.show()
        self.close()


class GuestInput(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        label_name = QLabel('Your Name', self)
        label_name.setFont(QFont('Eras Bold ITC'))
        label_name.setStyleSheet('font: bold 30px; color: white;')
        label_name.move(510, 400)
        label_name.adjustSize()

        bg = QImage('bg_second.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(bg))

        self.line = QLineEdit(self)
        self.line.move(400, 450)
        self.line.resize(400, 100)
        self.line.setMaxLength(10)
        self.line.setAlignment(Qt.AlignCenter)
        self.line.setFont(QFont('Eras Bold ITC'))
        self.line.setStyleSheet('background-color: white;border-style: '
                                'outset;border-width: 2px;border-radius: '
                                '10px;border-color: red;font: bold 50px;'
                                'color: red;')

        self.setPalette(palette)
        self.resize(1200, 800)
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle('TYPE GAME')

    def next_window(self):
        self.openz = StartWindow()
        self.openz.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window_first = StartWindow()
    sys.exit(app.exec_())
