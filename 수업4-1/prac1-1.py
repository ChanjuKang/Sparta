from pymongo import MongoClient
client = MongoClient('localhost', 27017)
database = client.ck_practice
#
# database.people.insert_one({'name':'chan27','age':27})
# database.people.insert_one({'name':'chan','age':26})
#
# people_list = list(database.people.find())
# # print(people_list)
# # print(people_list[0]['name'])
#
# # for people in people_list:
# #     print(people)
#
finder = list(database.people.find({'name':'chan'},{'_id':0}))
# finder = database.people.find_one({'name':'chan'},{'_id':0})
print(finder)
