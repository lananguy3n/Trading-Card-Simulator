import random
from datetime import datetime
from secrets import token_hex
from pymongo import MongoClient

client = MongoClient("mongodb+srv://username:SWEpassword@sweproject.wweidor.mongodb.net/?retryWrites=true&w=majority")

card_db = client.get_database('card_db')
common = list(card_db.common_cards.find())
uncommon = list(card_db.uncommon_cards.find())
rare = list(card_db.rare_cards.find())
superRare = list(card_db.superRare_cards.find())

user_db = client.get_database('user_db')
users = user_db.user_collection


def setup():
    db = client.get_database('user_db')
    collection = db.user_collection

    return collection

# def openPack(collection, id):
#     pack = random.choices(['C', 'UC', 'R', 'SR'], [70, 20, 7, 3], k=5)
#
#     # data = {
#     #     "id": id,
#     #     "date": datetime.now(),
#     #     "pack": pack
#     # }
#
#     # get the user database
#     db = client.get_database('user_db')
#     collection = db.user_collection
#
#     # check if user already exists
#     # i couldn't be bothered to make a check for it, but we should make one
#
#     # assume that the user exists, based on their ID
#     user_info = {
#         'id' : id
#     }
#
#     #user_data = collection.find_one(user_info)
#     #print(user_data)
#
#     #print(result)
#     #collection.insert_one(data)
#     print(f"PACK OPENED {pack}")
#
#     card_db = client.get_database('card_db')
#     common = list(card_db.common_cards.find())
#     uncommon = list(card_db.uncommon_cards.find())
#     rare = list(card_db.rare_cards.find())
#     superRare = list(card_db.superRare_cards.find())
#
#     user_common = []
#     user_uncommon = []
#     user_rare = []
#     user_superRare = []
#
#     #print(result)
#     #collection.insert_one(data)
#
#     # for each card pulled, generate a card of that rarity
#     for card in pack:
#         if card == "C":
#             user_common.append(random.choice(common))
#         elif card == "UC":
#             user_uncommon.append(random.choice(uncommon))
#         elif card == "R":
#             user_rare.append(random.choice(rare))
#         else:
#             user_superRare.append((random.choice(superRare)))
#
#     result = {"C" : user_common,
#               "UC" : user_uncommon,
#               "R" : user_rare,
#               "SR" : user_superRare}
#
#     data = {
#         "id": id,
#         "date": datetime.now(),
#         "pack": result
#     }
#
#     #print(result)
#     collection.insert_one(data)

def createUser(id):
    user_data = users.find({"id" : id})

    # user isn't already in system
    if (len(list(user_data))) == 0:

        # user's initial set
        # if we want to give all users a free initial card, we could
        result = {"C": [],
                  "UC": [],
                  "R": [],
                  "SR": []}

        # dictionary of initial user data
        data = {
            "id": id,
            "cards": result
        }

        # insert it in the system
        users.insert_one(data)

def openPack(id):
    pack = random.choices(['C', 'UC', 'R', 'SR'], [70, 20, 7, 3], k=5)

    user_data = users.find_one({"id" : id})
    user_cards = user_data.get("cards")

    for card in pack:
        if card == "C":
            user_cards.get("C").append(random.choice(common))
        elif card == "UC":
            user_cards.get("UC").append(random.choice(uncommon))
        elif card == "R":
            user_cards.get("R").append(random.choice(rare))
        else:
            user_cards.get("SR").append(random.choice(superRare))

    users.update_one({"id" : id}, {"$set" : {"cards" : user_cards}})

def viewUserCards(id):
    user_data = users.find_one({"id": id})
    user_cards = user_data.get("cards")

    rarities = ["C", "UC", "R", "SR"]

    for rarity in rarities:
        print(f"rarity {rarity}:\n")
        for card in user_cards.get(rarity):
            print(card)
        print("----------")

def printAllCards():
    print(list(common.find()))
    print(list(uncommon.find()))
    print(list(rare.find()))
    print(list(superRare.find()))

def main():
    id = input("user id: \n")
    createUser(id)
    openPack(id)
    viewUserCards(id)
    print(token_hex(16))

    # OAUTH 0 ---> user authentication
    # NODEJS/REACT ----> Frontend
    # Python + Flask ---> Backend
    # MONGODB ---> Card Collection, Storage


if __name__ == "__main__":
    main()
    #printAllCards()



