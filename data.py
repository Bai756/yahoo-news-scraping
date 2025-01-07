import pymongo

MONGO_URI = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.7"
MONGO_DATABASE = "news_db"
COLLECTION_NAME = 'news'

client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DATABASE]
collection = db[COLLECTION_NAME]

for news in collection.find():
    title = news["title"]
    url = news["url"]
    source = news["source"]
    print(f"{title}\n{url}\n{source}\n")

client.close()
