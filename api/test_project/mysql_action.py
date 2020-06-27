from pymysql import connect
import json
import yaml

class DB():
    def __init__(self):
        print('connect db...')
        self.conn = connect(host='127.0.0.1', user='root', password='bb961202', db='django_restful')

    # 清除表
    def clear(self, table_name):
        print('clear db...')
        clear_sql = 'truncate' + ' ' + table_name + ';'
        with self.conn.cursor() as cursor:
            cursor.execute('set foreign_key_checks=0;')
            cursor.execute(clear_sql)
        self.conn.commit()

    # 添加表
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        print(key)
        print(value)
        insert_sql = 'insert into' + ' ' + table_name + '(' + key + ')' + 'values' + '(' + value + ')'
        print(insert_sql)
        with self.conn.cursor() as cursor:
            cursor.execute(insert_sql)
        self.conn.commit()

    # 关闭数据库
    def close(self):
        print('close db')
        self.conn.close()

    # 初始化数据
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data():
                self.insert(table, d)
        self.close()


if __name__ == '__main__':
    db = DB()
    # db.clear('api_user')
    # user_data = {'id': 1, 'username': 'wulei', 'email': '1059457506@qq.com','groups':'team'}
    # db.insert('api_user', user_data)
    db.close()
    # file = open("datas.json", "r")
    # datas = json.load(file)
    # db.init_data(datas)
    # file = open("datas.yaml", "r")
    # datas = yaml.load(file,L)
    # db.init_data(datas)
