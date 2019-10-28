# -*- coding: utf-8 -*-
from MD import MD_win
if __name__ == '__main__':
    app = MD_win.QApplication(MD_win.sys.argv)
    main_win = MD_win.MD_window()
    main_win.show()
    MD_win.sys.exit(app.exec_())
