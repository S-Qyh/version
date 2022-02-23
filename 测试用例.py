from faker import Faker


from Data_course.代码.database import Sql

fk = Faker('zh_CN')
# print(fk.name())
# print(fk.phone_number())
# print(fk.password(length=6,special_chars=False,digits=True,upper_case=False,lower_case=True))
n = int(input("输入要生产的个数："))
for i in range(n):
    jibie = '2'
    name = fk.name()
    phone = fk.phone_number()
    password = fk.password(length=6, special_chars=False, digits=True, upper_case=False, lower_case=True)  # length：密码长度；special_chars：是否能使用特殊字符；digits：是否包含数字；upper_case：是否包含大写字母；lower_case：是否包含小写字母
    sql = "insert into 普通用户表(id,用户名, 密码, 电话, 用户级别) values('%s','%s','%s','%s','%s')" % (i,name, password, phone, jibie)
    Sql.sql2(sql)


