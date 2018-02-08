#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from PyQt5 import uic, QtWidgets

(from_class, qtbase_class) = uic.loadUiType('cal.ui')
print(from_class, qtbase_class)

class MainWindow(from_class, qtbase_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.addfunction)

    def addfunction(self):
        a = float(self.textEdit.toPlainText())
        b = float(self.textEdit_2.toPlainText())
        c = a + b
        self.textEdit_3.setText(str(c))
        self.textBrowser.append('{:.2f} + {:.2f} = {:.2f}'.format(a, b, c))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
