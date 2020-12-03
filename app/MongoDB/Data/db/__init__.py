from pymongo import MongoClient
from abc import ABC


client = MongoClient('mongodb://root:s3cr37@localhost:27027')
db = client.classic

class ResultList(list):
    def first_or_none(self):
        return self[0] if len(self) > 0 else None

    def last_or_none(self):
        return self[-1] if len(self) > 0 else None

class Document(dict, ABC):
    collection = None

    def __init__(self, data):
        super().__init__()
        if '_id' not in data:
            self._id = None
        self.__dict__.update(data)

    def __repr__(self):
        return '\n'.join(f'{k} = {v}' for k, v in self.__dict__.items())

    def save(self):
        if not self._id:
            del(self.__dict__['_id'])
            return self.collection.insert_one(self.__dict__)
        else:
            return self.collection.update({'_id': self._id}, self.__dict__)

    def delete_field(self, field):
        self.collection.update({'_id': self._id}, {"$unset": {field: ""}})


    @classmethod
    def insert_many(cls, items):
        for item in items:
            cls(item).save()

    @classmethod
    def all(cls):
        return [cls(item) for item in cls.collection.find({})]

    @classmethod
    def find(cls, **kwargs):
        return ResultList(cls(item) for item in cls.collection.find(kwargs))

    @classmethod
    def delete(cls, **kwargs):
        cls.collection.delete_many(kwargs)






