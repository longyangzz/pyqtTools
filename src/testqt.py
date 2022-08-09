# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 17:46:03 2022

@author: Administrator
"""
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 添加菜单
        menubar = self.menuBar();
        # 往菜单栏添加菜单项目
        file = menubar.addMenu("文件")
        # 给菜单项目添加子菜单
        newA = file.addAction("新建")
        saveA = file.addAction("保存")

        newA.triggered.connect(self.showAction)

    def showAction(self, curAction):
        print(curAction.name())



if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setWindowTitle("鼎创数据处理系统")
    window.setMinimumSize(800, 600)
    window.show()

    sys.exit(app.exec_())
