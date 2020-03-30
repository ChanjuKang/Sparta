import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser') #DATA,text는 웹에서 받는 html
#분석된 html 파일이 soup에 들어가있는 상태
print(soup)
# movies = soup.select('#old_content > table > tbody > tr')
# rank = 0
# #
# for movie in movies:
#     a_tag = movie.select_one('td.title>div>a')
#     star_tag = movie.select_one('td.point')
#     # rank_tag = movie.select_one('')
#     if a_tag is not None :
#         rank = rank +1
#         print('제목 : '+ str(a_tag.text) + ', 평점 :' + str(star_tag.text) + ', 순위 :' + str(rank))

