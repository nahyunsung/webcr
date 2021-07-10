# 네이버 날씨 화면 구성

import tkinter as tk
import requests
from bs4 import BeautifulSoup

win = tk.Tk()
win.title('네이버 날씨')
win.geometry("300x200")

def get_code(t_u):
    resp = requests.get(t_u)
    soup = BeautifulSoup(resp.text, 'html.parser')
    return soup


def n_weather():
    # 네이버 추출 정보 문자열로 반환
    # get_code(): 구문 정리한 태그 반환
    url = 'https://weather.naver.com/today/02173610'
    tag = get_code(url)

    # tag에서 필요 정보를 msg변수에 문자로 추출
    msg = ''
    tmp_area = tag.find('div', class_='weather_area')
    temp = tmp_area.find('strong').text
    msg += temp
    i_title = tmp_area.find_all('dt')
    i_data = tmp_area.find_all('dd')
    for idx, one in enumerate(i_title):
        title = one.text
        data = i_data[idx].text
        msg += f'\n{title}: {data}'
    return msg


def get_weather():
    # 1. 네이버 날씨에서 정보 추출
    msg = n_weather()
    # 2. 추출한 정보를 레이블에 출력
    lbl_info.config(text=msg)


def get_loc():
    url = 'https://weather.naver.com/today/02173610'
    tag = get_code(url)
    location = tag.find('strong', class_='location_name').text
    return location


loc = get_loc()

# 위젯 생성
lbl_lc = tk.Label(win, text=loc, font=('', 15))
lbl_info = tk.Label(win, text='')
btn_show = tk.Button(win, text="날씨 보기", command = get_weather)

lbl_lc.pack()
lbl_info.pack()
btn_show.pack()

win.mainloop()