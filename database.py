import pymysql


class Sql:

    def sql1(self):
        host = 'rm-bp150844nyaa96l67ao.mysql.rds.aliyuncs.com'
        port = 3306
        user = 'qyh'
        password = 'QYHqyh10215X'
        db = 'qyh'
        charset = 'utf8mb4'
        conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset)
        cur = conn.cursor()
        cur.execute(self)   # 提交命令
        fanhui = cur.fetchall()
        cur.close()
        conn.close()
        if fanhui == []:
            fanhui=[('',),]
        return fanhui

    def sql2(self):
        host = 'rm-bp150844nyaa96l67ao.mysql.rds.aliyuncs.com'
        port = 3306
        user = 'qyh'
        password = 'QYHqyh10215X'
        db = 'qyh'
        charset = 'utf8mb4'
        conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset)
        cur = conn.cursor()
        cur.execute(self)
        conn.commit()
        cur.close()
        conn.close()

# sql = "select id from 普通用户表 where id = '0'"
# a = Sql.sql1(sql)
# print(a)