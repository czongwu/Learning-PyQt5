'''
QLineEditEchoMode
QLineEdit控件回显模式

基本功能：输入单行的文本
EchoMode（回显模式）

4种回显模式

1、Normal
2、NoEcho
3、Password
4、PasswordEchoOnEdit
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class QLineEditEcho(QWidget):
    def __init__(self):
        super(QLineEditEcho, self).__init__()
        self.initUI()

    def initUI(self):
        FromLayout = QFormLayout()

        NormalLineEdit = QLineEdit()
        NoEchoLineEdit = QLineEdit()
        PasswordLineEdit = QLineEdit()
        PasswordEchoOnLineEdit = QLineEdit()

        FromLayout.addRow('Normal', NormalLineEdit)
        FromLayout.addRow('NoEcho', NoEchoLineEdit)
        FromLayout.addRow('Password', PasswordLineEdit)
        FromLayout.addRow('PasswordEchoOn', PasswordEchoOnLineEdit)

        # 设置提示文本
        NormalLineEdit.setPlaceholderText('Normal')
        NoEchoLineEdit.setPlaceholderText('NoEcho')
        PasswordLineEdit.setPlaceholderText('Password')
        PasswordEchoOnLineEdit.setPlaceholderText('PasswordEchoOn')

        # 设置LineEdit模式
        NormalLineEdit.setEchoMode(QLineEdit.Normal)
        NoEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        PasswordLineEdit.setEchoMode(QLineEdit.Password)
        PasswordEchoOnLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setWindowTitle('文本输入框的四种回显模式')
        self.setLayout(FromLayout)


icon = '/Users/chenzongwu/Documents/Learning-PyQt5/learning/img/konglong.ico'
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(icon))
    mainwin = QLineEditEcho()
    mainwin.show()
    sys.exit(app.exec_())
