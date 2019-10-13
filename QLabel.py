# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QMainWindow, QPushButton, QApplication, QToolTip, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont, QPalette, QPixmap
from PyQt5.QtCore import Qt, QRect


class QLabelDeamo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        button1 = QPushButton('退出')

        label1.setText('<font color=yellow>这是一个文本标签。</font>')
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.gray)  # 设置背景色
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)  # 设置文字对其方式

        label2.setText("<a href='#'>努力学习Python GUI程序</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap('./img/python.jpg'))

        label4.setOpenExternalLinks(True)  # 当bool值为True时，浏览器打开网页，当值为False时，响应槽方法
        label4.setText("<a href='https://zwcloud.top'>陈宗武的个人博客</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超级链接')

        button1.setToolTip('点击按钮退出程序')
        button1.clicked.connect(self.onClick_Button)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(button1)
        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkCliked)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件示例')
        self.setWindowIcon(QIcon('./img/konglong.ico'))
        self.resize(640, 480)


    def linkHovered(self):
        print('当鼠标滑过Label2时，触发事件')

    def linkCliked(self):
        print('当鼠标点击Label4时，触发事件')

    def onClick_Button(self):
        sender = self.sender()
        print(sender.text() + 'QLabel示例程序')
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('./img/konglong.ico'))
    main = QLabelDeamo()
    main.show()
    sys.exit(app.exec_())
