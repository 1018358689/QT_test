#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from PyQt5 import QtWidgets, uic

(a, b) = uic.loadUiType('002.ui')
class MainWindow(a,b):
    def __init__(self):
        super().__init__()
        self.setpUi(self)