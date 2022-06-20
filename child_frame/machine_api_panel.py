# -*- coding: utf-8 -*-
import sys
import os
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *

from .machine_api_ui import Ui_Form  # 由.UI文件生成.py文件后，导入创建的GUI类
from .machine_utils.holetest import Compare


class MacinePanel(QtWidgets.QMainWindow, Ui_Form):

    # __init__: 析构函数，也就是类被创建后就会预先加载的项目。
    # 马上运行，这个方法可以用来对你的对象做一些你希望的初始化。
    def __init__(self):
        # 这里需要重载一下Login_window，同时也包含了QtWidgets.QMainWindow的预加载项。
        super(MacinePanel, self).__init__()
        self.setupUi(self)
        self.path_img = None
        self.current_img = None

        # 控件初始化
        self.label_init_img.setAlignment(Qt.AlignCenter)
        self.label_end_img.setAlignment(Qt.AlignCenter)

        # 实现菜单栏文件栏点击事件操作
        try:
            self.bt_machine_read_img.clicked.connect(self._open_img)
            self.bt_machine_start_check.clicked.connect(self.start_check_img)
        except Exception as e:
            print(e)

    def _open_img(self):
        '''
        打开图片
        '''
        try:
            self.path_img, _ = QFileDialog.getOpenFileName(
                self.centralWidget(), '打开图片文件', './', 'Image Files(*.png *.jpg *.bmp)')
            if self.path_img and os.path.exists(self.path_img):
                self.init_img_view()
            else:
                QMessageBox.warning(self.centralWidget(), '无效路径', '无效路径，请重新选择！')
        except Exception as e:
            print(e)

    def init_img_view(self):
        jpg = QtGui.QPixmap(self.path_img).scaled(self.label_init_img.width(), self.label_init_img.height())
        self.label_init_img.setPixmap(jpg)

        # 先在结果图片中显示原始图
        # self.label_end_img.setPixmap(jpg)

    def start_check_img(self):
        try:
            print(self.path_img)
            img = cv2.imread(self.path_img)
            result_img, result_value = Compare(img, 3.2, 4)

            Image1 = cv2.resize(result_img, (self.label_end_img.width(), self.label_end_img.height()), interpolation=cv2.INTER_AREA)
            shrink = cv2.cvtColor(Image1, cv2.COLOR_BGR2RGB)
            self.QtImg = QtGui.QImage(shrink.data,
                                      shrink.shape[1],
                                      shrink.shape[0],
                                      shrink.shape[1] * 3,
                                      QtGui.QImage.Format_RGB888)

            self.label_end_img.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))


            if len(result_value) >= 2:

                self.lineEdit_one_error_value.setText(str(result_value[0][0]))
                self.lineEdit_one_bore_value.setText(str(result_value[0][1]))
                if result_value[0][2] == 1:
                    self.label_one_yes.setStyleSheet("border-image: url(:/resources/images/green_led.png);")
                else:
                    self.label_one_no.setStyleSheet("border-image: url(:/resources/images/red_led.png);")

                self.lineEdit_two_error_value.setText(str(result_value[1][0]))
                self.lineEdit_two_bore_value.setText(str(result_value[1][1]))
                if result_value[1][2] == 1:
                    self.label_two_yes.setStyleSheet("border-image: url(:/resources/images/green_led.png);")
                else:
                    self.label_two_no.setStyleSheet("border-image: url(:/resources/images/red_led.png);")

        except Exception as e:
            print(e)






