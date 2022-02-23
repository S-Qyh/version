import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from admin import *

# class Admin_test(QMainWindow, Ui_Admin):
#     def __init__(self, parent= None):
#         super(Admin_test, self).__init__(parent)
#         self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = Admin_test()
    mywin.show()
    sys.exit(app.exec_())