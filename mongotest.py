import pymongo
client = pymongo.MongoClient("mongodb+srv://chhotu:bhootnagar@cluster0.osd6scd.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"shafeek"
    "email"'shfkzhr@gmail.com'
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

d = {
    "name":"shafeek"
    "email"'shfkzhr@gmail.com'
}
d = {
    "name":"shafeek"
    "email"'shfkzhr@gmail.com'
}
d = {
    "name":"shafeek"
    "email"'shfkzhr@gmail.com'
}
d = {
    "name":"shafeek"
    "email"'shfkzhr@gmail.com'
}