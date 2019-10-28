# -*- coding:utf-8 -*-

# 窗口的setWindowIcon方法用于设置窗口图标，只在Windows中可用
# QApplication中的setWindowIcon方法用于设置主窗口的图标和应用程序图标，但调用了窗口的setWindowIcon方法
# QApplication中的setWindowIcon方法就只能用于设置应用程序图标了

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class IconForm(QMainWindow):
    def __init__(self, parent=None):
        super(IconForm, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # 设置主窗口的标题
        self.setWindowTitle('窗口图标设置')

        # 设置窗口尺寸
        self.resize(640, 480)

        self.setWindowIcon(QIcon('./img/konglong.ico'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./img/konglong.ico'))
    main = IconForm()
    main.show()

    sys.exit(app.exec_())
