import requests
from bs4 import BeautifulSoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# print(soup)

list_song = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

rank = 0
for song in list_song:
    title = song.select_one('td.info > a.title.ellipsis')
    artist = song.select_one('td.info > a.artist.ellipsis')

    if title is not None:
        rank = rank + 1
        title_data = title.text.strip()
        artist_data = artist.text
        print('순위:' + str(rank) + ', 제목:'+str(title_data) + ', 아티스트:' + str(artist_data))
