# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *

from login_ui import Ui_Form_Login  # 由.UI文件生成.py文件后，导入创建的GUI类

from child_frame.machine_api_panel import *  # Main.py为 主窗口代码文件

# 登录用户和密码信息
USER_PWD = {
    'la_vie': 'password',
    'user': '1234'
}

class Login_window(QtWidgets.QMainWindow, Ui_Form_Login):

    # __init__: 析构函数，也就是类被创建后就会预先加载的项目。
    # 马上运行，这个方法可以用来对你的对象做一些你希望的初始化。
    def __init__(self):
        # 这里需要重载一下Login_window，同时也包含了QtWidgets.QMainWindow的预加载项。
        super(Login_window, self).__init__()
        self.setupUi(self)

        # 将点击事件与槽函数进行连接
        self.btn_login.clicked.connect(self.btn_login_fuc)
        self.bt_quit.clicked.connect(self.check_close_func)

        # 登录按钮 函数

    def btn_login_fuc(self):
        user_info = self.le_user_info.text()
        pwd_info = self.le_pwd_info.text()
        if USER_PWD.get(user_info) != pwd_info:
            QMessageBox.critical(self, 'Wrong', '账户或密码错误，请重新输入!')
        else:
            # 1打开新窗口
            Ui_Main.show()
            # 2关闭本窗口
            self.close()

    # 判断用户密码是否正确或者退出
    def check_close_func(self):
        self.close()


if __name__ == '__main__':  # 如果这个文件是主程序。
    app = QtWidgets.QApplication(sys.argv)  # QApplication相当于main函数，也就是整个程序（很多文件）的主入口函数。对于GUI程序必须至少有一个这样的实例来让程序运行。
    window = Login_window()  # 生成一个实例（对象）
    Ui_Main = MacinePanel()  # 生成主窗口的实例
    window.show()  # 有了实例，就得让它显示。这里的show()是QWidget的方法，用来显示窗口。
    sys.exit(app.exec_())  # 调用sys库的exit退出方法，条件是app.exec_()也就是整个窗口关闭。