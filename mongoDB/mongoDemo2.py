import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb1"]
mycol = mydb["sites1"]

mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}

x = mycol.insert_one(mydict)
print(x.inserted_id)