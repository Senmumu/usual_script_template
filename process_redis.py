# -*- coding:utf-8 -*-
"""redis conn"""
import redis
import settings


class ProcessRedis(object):
    def __init__(self, *args):
        self._r = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            password=settings.REDIS_PASSWORD
        )

    def pop_data(self, key):
        """pop some data in list
        key: redis_key"""
        return self._r.lpop(key)

    def push_data(self, key, data):
        """
       push some data to list
       key: redis key
       data : some data(one type of data or list)
        """
        self._r.lpush(key, data)
