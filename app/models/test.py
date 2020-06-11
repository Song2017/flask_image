from typing import Union

import pymongo
from pymongo import MongoClient


def get_db(client: MongoClient):
    db_list = client.list_database_names()
    # db_list = client.database_names()
    if "my_db" in db_list:
        print("数据库已存在！")
        my_db = client["my_db"]
    else:
        my_db = my_client["my_db"]
    return my_db


def get_collection(database):
    col_list = database.list_collection_names()
    # col_list = db.collection_names()
    if "sites" in col_list:  # 判断 sites 集合是否存在
        print("集合已存在！")
        my_col = database["sites"]
    else:
        my_col = database["sites"]
    return my_col


def insert(collection, data: Union[list, dict]):
    if type(data) is dict:
        x = collection.insert_one(data)
    else:
        x = collection.insert_many(data)
    print(x.inserted_id)


def find(collection, query_data: dict = None,
         fields: dict = None, all_data=False) -> list:
    fields = fields or {"_id": 0}
    query_data = query_data or {}
    ret = []
    if all_data:
        for data in collection.find():
            ret.append(data)
        return ret

    for data in collection.find(query_data, fields):
        ret.append(data)
    return ret


def update(collection, query, values, many=False) -> int:
    if many:
        x = collection.update_many(query, values)
    else:
        x = collection.update_one(query, values)
    return x.modified_count


def delete(collection, query, many=False) -> int:
    if many:
        x = collection.delete_many(query)
    else:
        x = collection.delete_one(query)
    return x.deleted_count


def sort(collection, query: dict = None, sort_fields: dict = None,
         asc=True) -> list:
    ret = []
    for doc in collection.find(query).sort(sort_fields, int(asc)):
        ret.append(doc)
    return ret


if __name__ == '__main__':
    my_client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = get_db(my_client)
    col = get_collection(db)

    my_list = [
        {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
        {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
        {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
        {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
        {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
    ]
    for record in my_list:
        insert(col, record)
    print('result', find(col, all_data=True))
    result = find(col, query_data={'name': 'Taobao'})
    print('Taobao', result)
    print('update', update(col, {'name': 'Taobao'}, {"alexa": "110"}))
    print('delete', delete(col, {'name': '知乎'}))
    print('result', find(col, all_data=True))
    print('sort', sort(col, all_data=True))
