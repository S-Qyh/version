# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication
from admin_user_menu import Admin_user_menu_test
from mail_menu import MainWindow_to_sender
from search_express import search_express
from admin_mail import admin_mail
import express_rc
import express_search_rc
import exit_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 30, 151, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(620, 20, 151, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(590, 450, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setObjectName("pushButton_close")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(320, 110, 122, 298))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_Mail = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Mail.setFont(font)
        self.pushButton_Mail.setObjectName("pushButton_Mail")
        self.verticalLayout.addWidget(self.pushButton_Mail)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_search_mail = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_search_mail.setFont(font)
        self.pushButton_search_mail.setObjectName("pushButton_search_mail")
        self.verticalLayout.addWidget(self.pushButton_search_mail)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_admin_user = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_admin_user.setFont(font)
        self.pushButton_admin_user.setObjectName("pushButton_admin_user")
        self.verticalLayout.addWidget(self.pushButton_admin_user)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton_admin_mail = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_admin_mail.setFont(font)
        self.pushButton_admin_mail.setObjectName("pushButton_admin_mail")
        self.verticalLayout.addWidget(self.pushButton_admin_mail)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_Mail.clicked.connect(self.toMail) # type: ignore
        self.pushButton_search_mail.clicked.connect(self.searchMail) # type: ignore
        self.pushButton_admin_user.clicked.connect(self.adminUser) # type: ignore
        self.pushButton_admin_mail.clicked.connect(self.adminMail) # type: ignore
        self.pushButton_close.clicked.connect(self.exit) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        icon = QIcon(":/newPrefix/express.png")
        self.pushButton_Mail.setIcon(icon)

        icon1 = QIcon(":/newPrefix/express_search.png")
        self.pushButton_search_mail.setIcon(icon1)
        size = QSize(40,50)
        self.pushButton_search_mail.setIconSize(size)

        icon2 = QIcon(":/newPrefix/exit.png")
        self.pushButton_close.setIcon(icon2)


    def toMail(self):
        self.mail_menu_province = MainWindow_to_sender()
        self.mail_menu_province.show()

    def searchMail(self):
        self.search_mail = search_express()
        self.search_mail.show()

    def adminUser(self):
        self.adminUser = Admin_user_menu_test()
        self.adminUser.show()

    def adminMail(self):
        self.admin_mail = admin_mail()
        self.admin_mail.show()


    def close(self):
        self.close()

    def exit(self):
        self.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "管理员界面"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#ff0000;\">管理员界面</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">用户：管理员</span></p></body></html>"))
        self.pushButton_close.setText(_translate("MainWindow", "退出"))
        self.pushButton_Mail.setText(_translate("MainWindow", "寄件"))
        self.pushButton_search_mail.setText(_translate("MainWindow", "查件"))
        self.pushButton_admin_user.setText(_translate("MainWindow", "管理用户"))
        self.pushButton_admin_mail.setText(_translate("MainWindow", "管理快递"))

class Admin_menu_test(QMainWindow, Ui_MainWindow):
    def __init__(self, parent= None):
        super(Admin_menu_test, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = Admin_menu_test()
    mywin.show()
    sys.exit(app.exec_())