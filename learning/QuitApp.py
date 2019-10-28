# -*- coding:utf-8 -*-
# QDesktopWidget
import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QPushButton, QApplication, QWidget
from PyQt5.QtGui import QIcon

class QuitApp(QMainWindow):
    def __init__(self):
        super(QuitApp, self).__init__()
        self.resize(480, 240)
        self.setWindowTitle('quitApp')

        # 添加button

        self.button1 = QPushButton('退出程序')
        self.button1.clicked.connect(self.onClick_Button)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    # 按钮单击事件方法
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text() + '按钮被按下')
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./img/konglong.ico'))
    main = QuitApp()
    main.show()
    sys.exit(app.exec_())
