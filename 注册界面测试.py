import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from register import *

# class Register_test(QMainWindow, Ui_register):
#     def __init__(self, parent= None):
#         super(Register_test, self).__init__(parent)
#         self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = Register_test()
    mywin.show()
    sys.exit(app.exec_())