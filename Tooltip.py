# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QWidget, QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QFont, QIcon


class Tooltip(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 12))
        self.setToolTip('今天是<b>星期六</b>')
        self.setGeometry(300, 300, 200, 300)
        self.setWindowTitle('设置控件提示信息')

        self.button1 = QPushButton('My Button')
        self.button1.setToolTip('这是一个按钮，Are you ok?')
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./img/konglong.ico'))
    main = Tooltip()
    main.show()
    sys.exit(app.exec_())
