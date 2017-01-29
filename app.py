from redis import Redis
from pymongo import MongoClient
import os
from sys import exit


client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
try:
    db = client.tododb
except Exception:
    print("Error with connection to MongoDB")
    exit()

try:
    redis = Redis(host='redis', port=6379)
except Exception:
    print("Error with connection to RedisDB")
    exit()


def first_running(redis):
    print("This is a first running!")
    #mongo
    book = {}
    book["title"] = "Docker-compose guide"
    book["year"] = 2017
    book["author"] = "Unknown"
    db.tododb.insert(book)
    #redis
    redis = redis.set("count", 1)



def running(items, redis):
    print("This app has to be ran before!")
    for key, value in items[0].items():
    	print(key, "=>", value)
    count = redis.incr("count")
    print("Ran {} times!".format(count))
 

if __name__ == "__main__":
    _items = db.tododb.find()
    items = [item for item in _items]
    if items == []:
        first_running(redis)
    else:
        running(items, redis)

