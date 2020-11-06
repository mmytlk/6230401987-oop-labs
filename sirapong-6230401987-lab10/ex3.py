import sys
from PyQt5.QtWidgets import *


class Exercise3(QWidget):
    def __init__(self):
        super().__init__()
        self.ui()

    def ui(self):
        btn_ok = QPushButton('OK', self)
        btn_cc = QPushButton('Cancel', self)

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1, 1, 4)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1, 1, 4)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 4)

        grid.addWidget(btn_ok, 8, 3)
        grid.addWidget(btn_cc, 8, 4)

        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle(f'Review by {sys.argv[1]}')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex2 = Exercise3()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
