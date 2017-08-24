# -*- coding: utf-8 -*-
"""
存储数据
Ryan Luo
"""
import os
import settings
import pymongo
try:
    # Python 3.x
    from urllib.parse import quote_plus
except ImportError:
    # Python 2.x
    from urllib import quote_plus
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


class PipelineItem(object):
    """存储数据"""

    def __init__(self, col_name):
        host = settings.MONGODB_HOST
        port = settings.MONGODB_PORT
        db_name = settings.MONGODB_DBNAME
        user = settings.MONGODB_USERNAME
        password = settings.MONGO_PASSWORD
        uri = "mongodb://%s:%s@%s:%s" % (
            quote_plus(user), quote_plus(password), host, port)
        client = pymongo.MongoClient(uri)
        db = client[db_name]
        self.collection = db[col_name]

    def process(self, data_json):
        """
        process data to mongo
        data_json: a json list or one json to save

        you can modify insert_one to insert_many to save a json list
        """

        self.collection.insert_one(data_json)
        print('save success')
