# coding:utf-8
import psycopg2
import psycopg2.errorcodes
import settings


class CoachConn(object):
    ''' 连接 CockroachDB '''

    def __init__(self):
        ''' 初始化 '''
        self._conn = psycopg2.connect(database=settings.CoachDB,
                                      user=settings.CoachUser,
                                      password=settings.CoachPassword,
                                      host=settings.CoachHost,
                                      port=settings.CoachPort,)
        self._conn.set_session(autocommit=True)

    def read_data(self, select_sql, *data):
        ''' 读取数据 '''
        with self._conn.cursor() as cur:
            cur.execute(select_sql, data)
            rows = cur.fetchall()
        return rows

    def update_data(self, update_sql, *data):
        ''' 更新数据 '''
        with self._conn.cursor() as cur:
            cur.executemany(update_sql, data)

    def insert_data(self, insert_sql, *data):
        ''' 插入数据 '''
        with self._conn.cursor() as cur:
            cur.executemany(insert_sql, data)

    def close(self):
        ''' close connect '''
        self._conn.close()
