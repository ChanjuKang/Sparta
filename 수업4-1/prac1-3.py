from pymongo import MongoClient
client = MongoClient('localhost', 27017)
database = client.ck_practice           #데이터베이스 세팅

movies = list(database.movies.find())

movie_avg = database.movies.find_one({'title':'어벤져스: 엔드게임'})
star_data = movie_avg['star']
# print(star_data)
database.movies.update_many({'star':star_data},{'$set':{'star':0}})

# for movie in movies:
#     if movie["star"]==star_data:
#         database.movies.
