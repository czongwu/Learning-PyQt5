# -*- coding: utf-8 -*-
from MD import MD_win
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QWidget()
    mainwindow.setWindowIcon(QIcon('./img/konglong.ico'))
    ui = MD_win.MD_window()
    mainwindow.show()
    sys.exit(app.exec_())