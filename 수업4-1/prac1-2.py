import requests
from bs4 import BeautifulSoup           #크롤링 세팅
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
database = client.ck_practice           #데이터베이스 세팅

#평점 페이지 HTML페이지 가져오기
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
movies = soup.select('#old_content > table > tbody > tr')

# HTML에서 제목, 평점 가져오기
for movie in movies:
    title_tag = movie.select_one('td.title > div > a')
    star_tag = movie.select_one('td.point')
    if title_tag is not None:
        title = title_tag.text
        star = star_tag.text
        #이름, 별점 디비에 한줄씩 넣기
        info = {'title':title, 'star':star}
        database.movies.insert_one(info)








