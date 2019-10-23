# -*- coding: utf-8 -*-
# 笔记示例文件
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class signal_and_slot(QWidget):  # 定义主类
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        button1 = QPushButton('退出')  # 新建Button
        # button1按钮的信号(.clicked)与槽(onClick_Button)绑定
        button1.clicked.connect(self.onClick_Button)

        # 窗口布局
        vbox = QVBoxLayout()
        vbox.addWidget(button1)
        self.setLayout(vbox)
        self.resize(300, 300)

    def onClick_Button(self):  # 定义点击事件
        sender = self.sender()
        print(sender.Text() + '点击事件')
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = signal_and_slot()
    main.show()
    sys.exit(app.exec_())
