# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_modify_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QLineEdit

from database import Sql


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 10, 151, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(620, 40, 161, 31))
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(220, 110, 361, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_name = QtWidgets.QLabel(self.layoutWidget)
        self.label_name.setObjectName("label_name")
        self.gridLayout_2.addWidget(self.label_name, 0, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout_2.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.label_password = QtWidgets.QLabel(self.layoutWidget)
        self.label_password.setObjectName("label_password")
        self.gridLayout_2.addWidget(self.label_password, 1, 0, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout_2.addWidget(self.lineEdit_password, 1, 1, 1, 1)
        self.label_phone = QtWidgets.QLabel(self.layoutWidget)
        self.label_phone.setObjectName("label_phone")
        self.gridLayout_2.addWidget(self.label_phone, 2, 0, 1, 1)
        self.lineEdit_phone = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.gridLayout_2.addWidget(self.lineEdit_phone, 2, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(520, 380, 158, 37))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_exit = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout.addWidget(self.pushButton_exit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.queding) # type: ignore
        self.pushButton_exit.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def queding(self):
        username = self.lineEdit_name.text()
        password = self.lineEdit_password.text()
        phone = self.lineEdit_phone.text()
        if username != '':
            sql = "select ????????? from ??????????????? where ????????? = '%s'" % username
            data = Sql.sql1(sql)
            if data:
                if password != '':
                    sql = "update ??????????????? set ??????='%s' where ?????????='%s'" %(password, username)
                    Sql.sql2(sql)
                    QMessageBox.information(self, "??????", "?????????"+username+'\n??????????????????', QMessageBox.Ok)
                else:
                    if phone != '':
                        sql = "update ??????????????? set ??????='%s' where ?????????='%s'" % (phone, username)
                        Sql.sql2(sql)
                        QMessageBox.information(self, "??????", "?????????" + username + '\n??????????????????', QMessageBox.Ok)
                    else:
                        if phone == '':
                            QMessageBox.information(self, "??????", "?????????????????????\n?????????????????????????????????", QMessageBox.Ok)
                        elif password == '':
                            QMessageBox.information(self, "??????", "?????????????????????\n?????????????????????????????????", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "??????", "??????????????????", QMessageBox.Ok)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "????????????"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#ff0000;\">????????????</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">????????????????????????</span></p></body></html>"))
        self.label_name.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">????????????????????????</span></p></body></html>"))
        self.label_password.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">???????????????</span></p></body></html>"))
        self.label_phone.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">???????????????</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "??????"))
        self.pushButton_exit.setText(_translate("MainWindow", "??????"))

class modify_user(QMainWindow, Ui_MainWindow):
    def __init__(self, parent= None):
        super(modify_user, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = modify_user()
    mywin.show()
    sys.exit(app.exec_())
