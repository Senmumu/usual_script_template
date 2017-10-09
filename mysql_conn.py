# -*- coding: utf-8 -*-
"""
操作mysql
Rickon Luo
13.8.2017
"""
import pymysql


class MySQLOperation(object):
    """操作mysql"""

    def __init__(self):
        self._connection = pymysql.connect(host=settings.MYSQL_HOST,
                                           user=settings.MYSQL_USER,
                                           password=settings.MYSQL_PASSWORD,
                                           db=MYSQL_DB,
                                           charset='utf8',
                                           cursorclass=pymysql.cursors.DictCursor
                                           )

    def select_data(self, *data_list):
        """
        选择数据
        """
        try:
            with self._connection.cursor() as cursor:
                # Read a sinfle record
                sql = "select id,company from hname  c where  c.translate_to is null limit 500"
                cursor.execute(sql)
                result = cursor.fetchall()
            #  print(result)
            return result
        finally:
            pass

    def update_data(self, data_list):
        """"更新数据"""
        try:
            with self._connection.cursor() as cursor:
                # Read a sinfle record
                sql = "update hname  c  set c.`translate_name`=%s,c.`translate_to`=%s where c.id=%s "
                cursor.executemany(sql, data_list)
            self._connection.commit()
        finally:
            pass

    def close(self):
        """关闭连接"""
        self._connection.close()
