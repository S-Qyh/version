# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QLineEdit, QMessageBox, QMainWindow
from database import *
from admin_menu import Admin_menu_test
import login_rc
import exit_rc


class Ui_Admin(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 80, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 340, 75, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(250, 190, 251, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 340, 75, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.myBtnClick) # type: ignore
        self.pushButton.clicked.connect(self.myBtnClickTologin) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        icon = QIcon(':/newPrefix/login.png')
        self.pushButton.setIcon(icon)

        icon = QIcon(':/newPrefix/exit.png')
        self.pushButton_2.setIcon(icon)




    def close(self):
        self.close()

    def myBtnClick(self):
        self.close()

    def showAdminMenu(self):
        self.admin_menu = Admin_menu_test()
        self.admin_menu.show()

    def myBtnClickTologin(self):
        input_username = self.lineEdit.text()
        input_password = self.lineEdit_2.text()
        sql = "select 用户名 from 管理员用户表 where 用户名 = '%s' and 密码='%s'" % (input_username,input_password)
        a = Sql.sql1(sql)
        if a:
            QMessageBox.information(self, "消息", "用户名"+input_username+'密码正确', QMessageBox.Ok)
            '''
            在这里添加跳转界面
            '''
            # self.close()
            self.showAdminMenu()
        else:
            QMessageBox.information(self, "消息", "用户名"+input_username+'密码错误', QMessageBox.No)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "管理员登录"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">管理员登录</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "退出"))
        self.label_2.setText(_translate("MainWindow", "用户名："))
        self.label_3.setText(_translate("MainWindow", "密码："))
        self.pushButton.setText(_translate("MainWindow", "登录"))

class Admin_test(QMainWindow, Ui_Admin):
    def __init__(self, parent= None):
        super(Admin_test, self).__init__(parent)
        self.setupUi(self)
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = Admin_test()
    mywin.show()
    sys.exit(app.exec_())
