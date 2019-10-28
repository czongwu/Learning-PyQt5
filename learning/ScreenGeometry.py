# -*- coding:utf-8 -*-d
import sys
from PyQt5.QtWidgets import QHBoxLayout, QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtGui import QIcon


def onClick_Button():
    print("1")
    print('x: = %d' % widget.x())
    print('y: = %d' % widget.y())
    print('width = %d' % widget.width())
    print('height = %d \n' % widget.height())

    print("2.工作区坐标系")
    print('x: = %d' % widget.geometry().x())
    print('y: = %d' % widget.geometry().y())
    print('width = %d' % widget.geometry().width())
    print('height = %d \n' % widget.geometry().height())

    print("3.坐标系")
    print('x: = %d' % widget.frameGeometry().x())
    print('y: = %d' % widget.frameGeometry().y())
    print('width = %d' % widget.frameGeometry().width())
    print('height = %d' % widget.frameGeometry().height())


app = QApplication(sys.argv)
app.setWindowIcon(QIcon('./img/konglong.ico'))

widget = QWidget()
btn = QPushButton(widget)
btn.setText('Button')
btn.clicked.connect(onClick_Button)

btn.move(24, 52)
widget.resize(400, 250)  # 工作区的尺寸
widget.setWindowTitle('屏幕坐标系')

widget.show()
sys.exit(app.exec_())
