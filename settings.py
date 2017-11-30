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
REDIS_HOST = 'some_host_string'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

# Mysql Settings 
MYSQL_HOST = '192.168.0.110'
MYSQL_PORT = 3306
MYSQL_DBNAME = "some_db"
MYSQL_USERNAME = "username"
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')

#Neo4j Setings
NEO4J_HOST = '192.168.0.97'
NEO4J_PORT = 7474
#NEO4J_DBNAME = "disease"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')
