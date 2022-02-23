import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import QVariant

from area import dictPorovince, dictCity, dicTown
from database import Sql
from mail_menu_base import Ui_select
from test_lujing import lujing2


class MainWindow_to_sender(QWidget, Ui_select):
    def __init__(self, parent=None, *args, **kwargs):
        super(MainWindow_to_sender, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('省市区县联动部件')
        self.pushButton_ok.setDisabled(True)
        self.init_province()
        self.init_province1()
        self.init_signal_slot()

    # 初始化信号与槽函数，主要是选择框被激活及按扭框被点击事件信号
    def init_signal_slot(self):
        self.comboBox_province.activated.connect(self.add_city)
        self.comboBox_city.activated.connect(self.add_town)
        self.comboBox_town.activated.connect(self.just_btn_enable)
        self.pushButton_ok.clicked.connect(self.btn_ok)

        self.comboBox_province_2.activated.connect(self.add_city2)
        self.comboBox_city_2.activated.connect(self.add_town2)
        self.comboBox_town_2.activated.connect(self.just_btn_enable2)

    # 初始化省份的数据
    def init_province(self):
        provinces = dictPorovince.values()
        # print(provinces)
        self.comboBox_province.clear()
        self.comboBox_province.addItem('请选择')
        for key, value in dictPorovince.items():
            self.comboBox_province.addItem(value, QVariant(key))

    # 当省份按钮被选择后添加对应的城市数据
    def add_city(self, index):
        pro_code = self.comboBox_province.itemData(index)
        city = dictCity.get(pro_code, dict())
        self.comboBox_city.clear()
        self.comboBox_city.addItem('请选择')
        self.comboBox_town.clear()
        self.comboBox_town.addItem('请选择')
        if self.comboBox_province.currentText() != '请选择':
            for key, value in city.items():
                self.comboBox_city.addItem(value, QVariant(key))
        self.pushButton_ok.setDisabled(True)

    # 当城市按钮被选择后添加对应的区县数据
    def add_town(self, index):
        city_code = self.comboBox_city.itemData(index)
        town = dicTown.get(city_code, dict())
        self.comboBox_town.clear()
        self.comboBox_town.addItem('请选择')
        if self.comboBox_city.currentText() != '请选择':
            for key, value in town.items():
                self.comboBox_town.addItem(value, QVariant(key))
        self.pushButton_ok.setDisabled(True)

    def just_btn_enable(self, txt):
        if self.comboBox_town.currentText() != '请选择':
            self.pushButton_ok.setDisabled(False)
        else:
            self.pushButton_ok.setDisabled(True)

    def btn_ok(self):
        self.selection = '寄件人省份：{}，城市：{}，区县：{},详细地址：{}\n收件人省份：{}，城市：{}，区县：{},详细地址：{}'.format(
            self.comboBox_province.currentText(),
            self.comboBox_city.currentText(),
            self.comboBox_town.currentText(),
            self.lineEdit.text(),
            self.comboBox_province_2.currentText(),
            self.comboBox_city_2.currentText(),
            self.comboBox_town_2.currentText(),
            self.lineEdit_2.text()
        )
        jichu_province = self.comboBox_province.currentText()
        jichu_city = self.comboBox_city.currentText()
        jichu_town = self.comboBox_town.currentText()
        jichu_adress = self.lineEdit.text()
        jichu_phone = self.lineEdit_3.text()
        jichu_name = self.lineEdit_5.text()

        shoujian_province = self.comboBox_province_2.currentText()
        shoujian_city = self.comboBox_city_2.currentText()
        shoujian_town = self.comboBox_town_2.currentText()
        shoujian_adress = self.lineEdit_2.text()
        shoujian_phone = self.lineEdit_4.text()
        shoujian_name = self.lineEdit_6.text()

        jichu_city = jichu_city + '市'
        shoujian_city = shoujian_city + '市'

        express_id = ''
        sql = "select 市编 from 市表 where 市名='%s'" % jichu_city
        k1 = Sql.sql1(sql)

        express_id = express_id + k1[0][0]  # 寄出市市编为快递单号前四位

        sql = "select 市编 from 市表 where 市名='%s'" % shoujian_city
        k1 = Sql.sql1(sql)

        express_id = express_id + k1[0][0]  # 收件市 市编为快递单号5-8位

        sql = "select 快递单号 from 快递表 "
        k1 = Sql.sql1(sql)
        k1 = k1[-1][0]  # 查询数据库中最后一个快递单号

        if k1 == '':  # 如果数据库中没有快递单
            k1 = '100'  # 快递单最后3为为100
        else:  # 有快递单号 新快递单号后3位为上一个快递单号后3位+1
            k1 = k1[8:]
            # print(1, k1)
            k1 = int(k1) + 1
            # print(2, k1)
            k1 = str(k1)

        express_id += k1

        shoujian_adress = shoujian_province + shoujian_city + shoujian_town + shoujian_adress

        jichu_adress = jichu_province + jichu_city + jichu_town + jichu_adress

        beizhu = '1'
        # if lujing2[0] == '0':  # lujing2存储了省-省之间的路径 为0则为同省快递
        #
        #     if jichu_city != shoujian_city:  # 寄出城市不为收件城市
        #         beizhu = jichu_city + '-'
        #         sql = "select 省会城市 from 省份表 where 省份='%s'" % (jichu_province)
        #         k1 = Sql.sql1(sql)
        #         k1 = k1[0][0]
        #         if jichu_city != k1 and shoujian_city != k1:
        #             beizhu = beizhu + k1 + '-' + shoujian_city  # 收件城市不为省会 备注=寄出城市+省会城市+收件城市
        #         else:
        #             beizhu = jichu_city + '-' + shoujian_city  # 收件城市为省会 备注=寄出城市+收件城市
        #     else:
        #         beizhu = jichu_city + '-' + shoujian_city  # 同市快递
        # else:  # 跨省快递
        #
        #     if jichu_city != lujing2[0]:  # 寄出城市不为省会,将寄出城市放到首位
        #         beizhu = jichu_city + '-'
        #
        #     for x in lujing2:
        #         beizhu = beizhu + x + '-'
        #
        #     if shoujian_city != lujing2[-1]:  # 收件城市不为省会 将收件城市放到末尾
        #         beizhu = beizhu + shoujian_city
        #     else:
        #         beizhu = beizhu[:-1]
        #
        # print(beizhu)

        sql = "insert into 快递表(快递单号,寄出省,寄出市,寄出地址,寄件人姓名,寄件人手机号码,收件省,收件市,收件地址,收件人姓名, 收件人手机号码, 备注, 到达位置, 寄出位置) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s')" % (
            express_id, jichu_province, jichu_city, jichu_town, jichu_name, jichu_phone, shoujian_province,
            shoujian_city, shoujian_town, shoujian_name, shoujian_phone, beizhu, shoujian_adress, jichu_adress)

        Sql.sql2(sql)
        QMessageBox.information(self, '信息', self.selection, QMessageBox.Ok)
        QMessageBox.information(self, '信息', "邮寄成功！", QMessageBox.Ok)

        # 初始化省份的数据

    def init_province1(self):
        provinces = dictPorovince.values()
        # print(provinces)
        self.comboBox_province_2.clear()
        self.comboBox_province_2.addItem('请选择')
        for key, value in dictPorovince.items():
            self.comboBox_province_2.addItem(value, QVariant(key))

    def add_city2(self, index):
        pro_code = self.comboBox_province_2.itemData(index)
        city = dictCity.get(pro_code, dict())
        self.comboBox_city_2.clear()
        self.comboBox_city_2.addItem('请选择')
        self.comboBox_town_2.clear()
        self.comboBox_town_2.addItem('请选择')
        if self.comboBox_province_2.currentText() != '请选择':
            for key, value in city.items():
                self.comboBox_city_2.addItem(value, QVariant(key))
        self.pushButton_ok.setDisabled(True)

    def add_town2(self, index):
        city_code = self.comboBox_city_2.itemData(index)
        town = dicTown.get(city_code, dict())
        self.comboBox_town_2.clear()
        self.comboBox_town_2.addItem('请选择')
        if self.comboBox_city_2.currentText() != '请选择':
            for key, value in town.items():
                self.comboBox_town_2.addItem(value, QVariant(key))
        self.pushButton_ok.setDisabled(True)

    def just_btn_enable2(self, txt):
        if self.comboBox_town_2.currentText() != '请选择':
            self.pushButton_ok.setDisabled(False)
        else:
            self.pushButton_ok.setDisabled(True)

    def jijian_name(self):
        filename = "login_info.txt"
        with open(filename, 'r') as f:
            line = f.readline()
        username = line
        sql = "SELECT`普通用户表`.* FROM `普通用户表` WHERE `普通用户表`.`用户名` = '%s'" % username
        result1 = Sql.sql1(sql)
        # print(result1)
        userphone = result1[0][3]
        # print(result1)
        username = result1[0][1]
        self.lineEdit_3.setText(userphone)
        self.lineEdit_5.setText(username)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow_to_sender()
    window.show()
    sys.exit(app.exec_())
