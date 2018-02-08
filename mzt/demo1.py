#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from PyQt5 import uic, QtWidgets, QtGui
import requests

(a, b) = uic.loadUiType('001.ui')


class MainWindow(a, b):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self._showpic)

    def _showpic(self):
        # headers = {
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        #     'Accept-Encoding': 'gzip, deflate',
        #     'Accept-Language': 'zh-CN,zh;q=0.9',
        #     'Cache-Control': 'max-age=0',
        #     'Connection': 'keep-alive',
        #     'Host': 'img.mmjpg.com',
        #     'Referer': 'http://www.mmjpg.com/mm/1244',
        #     'Upgrade-Insecure-Requests': '1',
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        # }
        headers = {
            'Referer': 'http://www.mzitu.com/118659/2',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
        res = requests.get(url='http://i.meizitu.net/2018/02/02a02.jpg', headers=headers)
        pic = res.content
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(pic)
        self.label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
