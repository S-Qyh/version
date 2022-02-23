import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from user import *

# class User_test(QMainWindow, Ui_user):
#     def __init__(self, parent= None):
#         super(User_test, self).__init__(parent)
#         self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = User_test()
    mywin.show()
    sys.exit(app.exec_())