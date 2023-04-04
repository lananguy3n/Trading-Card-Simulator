from pymongo import MongoClient

client = MongoClient("mongodb+srv://username:SWEpassword@sweproject.wweidor.mongodb.net/?retryWrites=true&w=majority")

db = client.get_database('user_db')
collection = db.user_collection

new_card = {
    'name' : 'Troy',
    'number' : 2
}

collection.count_documents({})

print('test')
collection.insert_one(new_card)
print('test again')

####
# ID
# name
# card collection
