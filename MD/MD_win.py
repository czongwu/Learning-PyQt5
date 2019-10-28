# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MD_window(QWidget):
    def __init__(self):
        super(MD_window, self).__init__()
        self.edit_label = QLabel('TextEditor', self)
        self.browser_label = QLabel('TextBrowser', self)
        self.text_edit = QTextEdit(self)
        self.text_browser = QTextBrowser(self)
        self.setWindowIcon(QIcon('E:\Learning-PyQt5\img\konglong.ico'))

        self.edit_v_layout = QVBoxLayout()
        self.browser_v_layout = QVBoxLayout()
        self.all_h_layout = QHBoxLayout()

        self.layout_init()
        self.text_edit_init()

    def layout_init(self):
        self.edit_v_layout.addWidget(self.edit_label)
        self.edit_v_layout.addWidget(self.text_edit)

        self.browser_v_layout.addWidget(self.browser_label)
        self.browser_v_layout.addWidget(self.text_browser)

        self.all_h_layout.addLayout(self.edit_v_layout)
        self.all_h_layout.addLayout(self.browser_v_layout)

        self.setLayout(self.all_h_layout)

    def text_edit_init(self):
        self.text_edit.textChanged.connect(self.show_text_func)

    def show_text_func(self):
        self.text_browser.setText(self.text_edit.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MD_window()
    main_win.show()
    sys.exit(app.exec_())
