# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'machine_api_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(809, 427)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(310, 390, 61, 31))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(490, 390, 31, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(600, 390, 21, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_two_error_value = QtWidgets.QLineEdit(Form)
        self.lineEdit_two_error_value.setGeometry(QtCore.QRect(370, 390, 61, 31))
        self.lineEdit_two_error_value.setObjectName("lineEdit_two_error_value")
        self.bt_machine_read_img = QtWidgets.QPushButton(Form)
        self.bt_machine_read_img.setGeometry(QtCore.QRect(40, 370, 101, 31))
        self.bt_machine_read_img.setObjectName("bt_machine_read_img")
        self.bt_machine_start_check = QtWidgets.QPushButton(Form)
        self.bt_machine_start_check.setGeometry(QtCore.QRect(180, 370, 101, 31))
        self.bt_machine_start_check.setObjectName("bt_machine_start_check")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(440, 390, 21, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_two_bore_value = QtWidgets.QLineEdit(Form)
        self.lineEdit_two_bore_value.setGeometry(QtCore.QRect(530, 390, 61, 31))
        self.lineEdit_two_bore_value.setObjectName("lineEdit_two_bore_value")
        self.label_init_img = QtWidgets.QLabel(Form)
        self.label_init_img.setEnabled(True)
        self.label_init_img.setGeometry(QtCore.QRect(10, 20, 391, 291))
        self.label_init_img.setObjectName("label_init_img")
        self.label_end_img = QtWidgets.QLabel(Form)
        self.label_end_img.setEnabled(True)
        self.label_end_img.setGeometry(QtCore.QRect(410, 20, 391, 291))
        self.label_end_img.setStyleSheet("")
        self.label_end_img.setObjectName("label_end_img")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(490, 350, 31, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(600, 350, 21, 31))
        self.label_6.setObjectName("label_6")
        self.lineEdit_one_error_value = QtWidgets.QLineEdit(Form)
        self.lineEdit_one_error_value.setGeometry(QtCore.QRect(370, 350, 61, 31))
        self.lineEdit_one_error_value.setObjectName("lineEdit_one_error_value")
        self.lineEdit_one_bore_value = QtWidgets.QLineEdit(Form)
        self.lineEdit_one_bore_value.setGeometry(QtCore.QRect(530, 350, 61, 31))
        self.lineEdit_one_bore_value.setObjectName("lineEdit_one_bore_value")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(440, 350, 21, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(310, 350, 61, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(680, 350, 31, 31))
        self.label_9.setObjectName("label_9")
        self.label_one_yes = QtWidgets.QLabel(Form)
        self.label_one_yes.setGeometry(QtCore.QRect(640, 350, 31, 31))
        self.label_one_yes.setStyleSheet("border-image: url(:/resources/images/normal_led.png);")
        self.label_one_yes.setText("")
        self.label_one_yes.setObjectName("label_one_yes")
        self.label_one_no = QtWidgets.QLabel(Form)
        self.label_one_no.setGeometry(QtCore.QRect(720, 350, 31, 31))
        self.label_one_no.setStyleSheet("border-image: url(:/resources/images/normal_led.png);")
        self.label_one_no.setText("")
        self.label_one_no.setObjectName("label_one_no")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(760, 350, 41, 31))
        self.label_10.setObjectName("label_10")
        self.label_two_no = QtWidgets.QLabel(Form)
        self.label_two_no.setGeometry(QtCore.QRect(720, 390, 31, 31))
        self.label_two_no.setStyleSheet("border-image: url(:/resources/images/normal_led.png);")
        self.label_two_no.setText("")
        self.label_two_no.setObjectName("label_two_no")
        self.label_two_yes = QtWidgets.QLabel(Form)
        self.label_two_yes.setGeometry(QtCore.QRect(640, 390, 31, 31))
        self.label_two_yes.setStyleSheet("border-image: url(:/resources/images/normal_led.png);")
        self.label_two_yes.setText("")
        self.label_two_yes.setObjectName("label_two_yes")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(760, 390, 41, 31))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(680, 390, 31, 31))
        self.label_12.setObjectName("label_12")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "误差范围："))
        self.label_3.setText(_translate("Form", "孔径："))
        self.label_4.setText(_translate("Form", "MM"))
        self.bt_machine_read_img.setText(_translate("Form", "读取图片"))
        self.bt_machine_start_check.setText(_translate("Form", "开始检测"))
        self.label_2.setText(_translate("Form", "MM"))
        self.label_init_img.setText(_translate("Form", "原始图片"))
        self.label_end_img.setText(_translate("Form", "结果图片"))
        self.label_5.setText(_translate("Form", "孔径："))
        self.label_6.setText(_translate("Form", "MM"))
        self.label_7.setText(_translate("Form", "MM"))
        self.label_8.setText(_translate("Form", "误差范围："))
        self.label_9.setText(_translate("Form", "合格"))
        self.label_10.setText(_translate("Form", "不合格"))
        self.label_11.setText(_translate("Form", "不合格"))
        self.label_12.setText(_translate("Form", "合格"))
import apprcc_rc
