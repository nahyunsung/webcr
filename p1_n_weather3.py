import tkinter as tk
import requests
from bs4 import BeautifulSoup

win = tk.Tk()
win.title("날씨 정보")
win.geometry("300x200")


def get_tag(t_u):
    resp = requests.get(t_u)
    sp = BeautifulSoup(resp.text, 'html.parser')
    return sp


url = 'https://weather.naver.com/today/02173610'
soup = get_tag(url)


def get_temp():
    loc = soup.find('strong', class_='location_name').text
    temp = soup.find('strong', class_='current').text
    lbl_loc.config(text=loc)
    lbl_temp.config(text=temp)


def get_dust():
    msg = ''
    dust = soup.find_all('strong', class_='ttl')
    dust_s = soup.find_all('em', class_='level_text')
    for idx, one in enumerate(dust_s):
        title = dust[idx].text
        s = one.text
        msg += f'{title}: {s}\n'
    lbl_dust.config(text=msg)


lbl_loc = tk.Label(win, text='')
lbl_temp = tk.Label(win, text='')
btn_dust = tk.Button(win, text='미세먼지 확인', command = get_dust)
lbl_dust = tk.Label(win, text='')

get_temp()

lbl_loc.pack()
lbl_temp.pack()
btn_dust.pack()
lbl_dust.pack()

win.mainloop()