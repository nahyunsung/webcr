import requests
from bs4 import BeautifulSoup

# 1.웹페이지 주소 설정
user = input('번역할 단어: ')
url = 'https://dic.daum.net/search.do?q='+ user

# 2. 페이지 요청하기
resp = requests.get(url)

# 3. 페이지 구문 분석
soup = BeautifulSoup(resp.text, 'html.parser')
# 4. 정보 추출 (cleanword_type kuek_type)
block = soup.find('div', class_="cleanword_type kuek_type")
worlds = block.find_all('li')

# 5 정보 출력
for one in worlds:
    print(one.text)