# -*- coding: utf-8 -*-
"""相关设置"""
import os

# MongoDB Settings
MONGODB_HOST = "some_host_string"
MONGODB_PORT = 27017
MONGODB_DBNAME = 'some_db'
MONGODB_USERNAME = 'username'
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')


# Redis Settings
REDIS_HOST = '192.168.0.202'
REDIS_PORT = 27017
REDIS_DB = 'uptodate_com'
REDIS_PASSWORD = os.getenv('MONGO_PASSWORD')
