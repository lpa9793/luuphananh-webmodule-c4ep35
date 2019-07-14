import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient('mongodb://admin:admin@ds021182.mlab.com:21182/c4e')
db = client.c4e
db.posts.insert_one({'title': 'Những người khốn khổ','author': 'Luu Phan Anh','content': 'Sự nghiệp coding thật lắm gian truân'})