# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 22:54:26 2020

@author: ganglim
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class myApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        label1 = QLabel('Label1', self)
        label1.move(20, 20)
        label2 = QLabel('label2', self)
        label2.move(20, 60)
        
        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)
        
        
        self.setWindowTitle('Absolute Positioning')
        self.setGeometry(300, 300, 400, 200)
        self.show()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = myApp()
    sys.exit(app.exec_())