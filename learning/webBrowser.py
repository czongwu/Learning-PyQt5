# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWebEngineWidgets, QtCore


class webBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # QToolTip.setFont(QFont('SansSerif', 12))
        # self.setToolTip('今天是<b>星期六</b>')
        self.setGeometry(480, 100, 1024, 768)
        self.setWindowTitle('zw浏览器')
        self.webEngineView = QtWebEngineWidgets.QWebEngineView()
        self.webEngineView.setUrl(QtCore.QUrl("https://www.zwcloud.top/"))

        self.button1 = QPushButton('My Button')
        # self.button1.setToolTip('这是一个按钮，Are you ok?')
        layout = QHBoxLayout()
        # layout.addWidget(self.button1)
        layout.addWidget(self.webEngineView)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./img/konglong.ico'))
    main = webBrowser()
    main.show()
    sys.exit(app.exec_())
