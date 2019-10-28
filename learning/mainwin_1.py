# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class mainwin_1(QMainWindow):
    def __init__(self, parent=None):
        super(mainwin_1, self).__init__(parent)

        # 设置主窗口的标题
        self.setWindowTitle('mainwindow_1')

        # 设置窗口尺寸
        self.resize(640, 480)

        self.status = self.statusBar()

        self.status.showMessage('5s消息窗', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./img/konglong.ico'))
    main = mainwin_1()
    main.show()

    sys.exit(app.exec_())
