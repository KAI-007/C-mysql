# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CK.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1186, 884)
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1181, 871))
        self.graphicsView.setStyleSheet("border-image: url(:/newPrefix/ditu.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 54, 12))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(60, 10, 141, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 10, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 10, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 10, 111, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(620, 10, 111, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 290, 75, 23))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(320, 600, 75, 23))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(830, 430, 75, 23))
        self.pushButton_7.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 80, 201, 261))
        self.textBrowser.setObjectName("textBrowser")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(60, 50, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(300, 20, 71, 16))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "车间监控"))
        self.comboBox.setItemText(0, _translate("Form", "1号车间"))
        self.comboBox.setItemText(1, _translate("Form", "2号车间"))
        self.comboBox.setItemText(2, _translate("Form", "3号车间"))
        self.pushButton.setText(_translate("Form", "开始"))
        self.pushButton_2.setText(_translate("Form", "监控图表"))
        self.pushButton_3.setText(_translate("Form", "数据管理"))
        self.pushButton_4.setText(_translate("Form", "先检测一波"))
        self.pushButton_5.setText(_translate("Form", "1号车间"))
        self.pushButton_6.setText(_translate("Form", "2号车间"))
        self.pushButton_7.setText(_translate("Form", "3号车间"))
        self.comboBox_2.setItemText(0, _translate("Form", "115200"))
        self.checkBox.setText(_translate("Form", "CheckBox"))
import dt_rc
