from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##
avg = db.movies.find_one({'title':'어벤져스: 엔드게임'})
target_star = avg['star']


movies = list(db.movies.find({'star': target_star}))
    print(movies)

    # db.movies.update_one({'star': 0}, {'$set':{'star':1}})
    # print(movie['title'])
