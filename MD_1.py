# -*- coding: utf-8 -*-
import MD_Mian
import sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QWidget()
    ui = MD_Mian.Ui_Form()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())