# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 22:35:05 2020

@author: ganglim
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        lb1_red = QLabel('Red')
        lb1_green = QLabel('Green')
        lb1_blue = QLabel('Blue')
        
        lb1_red.setStyleSheet("color: red;"
                              "border-style: solid;"
                              "border-width: 2px;"
                              "border-color: #FA8072;"
                              "border-radius:3px")
        lb1_green.setStyleSheet("color: green;"
                                "background-color: #7FFFD4")
        lb1_blue.setStyleSheet("color: bule;"
                               "background-color: #87CEFA;"
                               "border-style: dashed;"
                               "border-width: 3px;"
                               "border-color: #1E90FF")
        
        vbox = QVBoxLayout()
        vbox.addWidget(lb1_red)
        vbox.addWidget(lb1_green)
        vbox.addWidget(lb1_blue)
        
        self.setLayout(vbox)
        
        self.setWindowTitle('Stylesheet')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())