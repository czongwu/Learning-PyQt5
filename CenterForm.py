# -*- coding:utf-8 -*-
# QDesktopWidget
import sys
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class CenterForm(QMainWindow):
    def __init__(self, parent=None):
        super(CenterForm, self).__init__(parent)

        # 设置主窗口的标题
        self.setWindowTitle('窗口居中')

        # 设置窗口尺寸
        self.resize(640, 480)

        # self.status = self.statusBar()
        #
        # self.status.showMessage('5s消息窗', 5000)

    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = int((screen.width() - size.width()) / 2)
        newTop = int((screen.height() - size.height()) / 2)
        self.move(newLeft, newTop)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./img/konglong.ico'))
    main = CenterForm()
    main.show()

    sys.exit(app.exec_())
