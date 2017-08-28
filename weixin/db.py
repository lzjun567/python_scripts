from pymongo import MongoClient


class Conn(object):
    client = MongoClient('localhost', 27017)
    db = client['weixin-comment']

    @classmethod
    def insert_many(cls, data):
        cls.db['comments'].insert_many(data)

    @classmethod
    def query(cls):
        data = cls.db['comments'].find()
        return data


conn = Conn()
