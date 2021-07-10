# 네이버 날씨

import requests
from bs4 import BeautifulSoup

# 1. 웹페이지 주소 찾고 요청
url = 'https://weather.naver.com/today/02173610'
resp = requests.get(url)

# 2. 요청 받은 텍스트 구문 정리
soup = BeautifulSoup(resp.text, 'html.parser')

# 3. 정보 추출
# div : weather_area
w_area = soup.find('div', class_='weather_area')
temp = w_area.find('strong')
i_titles = w_area.find_all('dt')
i_data = w_area.find_all('dd')
lound = soup.find('strong', class_='location_name')

# 4. 정보 출력
print(lound.text)
print(temp.text)
# print(i_titles[0].text, ":", i_data[0].text)
# print(f"{i_titles[0].text} : {i_data[0].text}")
# print("{}: {}".format(i_titles[0].text, i_data[0].text))

# 출력 양식 변경
for idx, one in enumerate(i_titles):
    # print(idx, one.text, i_data[idx].text)
    title = one.text
    data = i_data[idx].text
    print(f'{title}: {data}')