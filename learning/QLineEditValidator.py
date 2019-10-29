'''
限制QLineEdit控件的输入（校验器）
限制只能输入整数，浮点数或满足一定条件的字符串
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator, QIcon
from PyQt5.QtCore import QRegExp
import sys


class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本校验器（限制输入）')

        IntLineEdit = QLineEdit()
        DoubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        FromLayout = QFormLayout()

        FromLayout.addRow('整数类型', IntLineEdit)
        FromLayout.addRow('浮点类型', DoubleLineEdit)
        FromLayout.addRow('数字和字母', validatorLineEdit)

        IntLineEdit.setPlaceholderText('整数类型')
        DoubleLineEdit.setPlaceholderText('浮点类型')
        validatorLineEdit.setPlaceholderText('数字和字母')

        # 整数校验器
        intValidator = QIntValidator(self)
        intValidator.setRange(1, 99)

        # 浮点校验器
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-360, 360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)

        # 正则表达式 数字和字母
        validator = QRegExp('[a-zA-Z0-9]+&')
        RegValidator = QRegExpValidator(self)
        RegValidator.setRegExp(validator)

        # 设置校验器
        IntLineEdit.setValidator(intValidator)
        DoubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(RegValidator)

        self.setLayout(FromLayout)


if __name__ == '__main__':
   app = QApplication(sys.argv)
   app.setWindowIcon(QIcon('./img/konglong.ico'))
   mainwin = QLineEditValidator()
   mainwin.show()
   sys.exit(app.exec_())