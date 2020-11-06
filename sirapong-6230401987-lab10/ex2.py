import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class Exercise2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        file_menu = menubar.addMenu('File')

        imp_edit = QMenu('Edit', self)
        imp_act = QAction('Copy', self)
        imp_act2 = QAction('Paste', self)
        imp_edit.addAction(imp_act) 
        imp_edit.addAction(imp_act2)

        new_act = QAction('New', self)
        file_menu.addAction(new_act)
        file_menu.addMenu(imp_edit)

        save_act = QAction(QIcon(), 'Save', self)
        save_act.setShortcut('Ctrl+S')
        file_menu.addAction(save_act)

        quit_act = QAction(QIcon(), 'Quit', self)
        quit_act.setShortcut('Ctrl+Q')
        quit_act.triggered.connect(QApplication.instance().quit)
        file_menu.addAction(quit_act)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Exercise 2')
        self.statusBar().addPermanentWidget(QLabel(f'By {sys.argv[1]}'), 1), self.show()
        self.show()

def main():
    app = QApplication([sys.argv])
    ex2 = Exercise2()
    sys.exit(app.exec_())

if __name__ == "__main__":

    main()