import requests
from bs4 import BeautifulSoup
from tkinter import *

def fr():
    url = 'https://news.daum.net/'
    msg = ''
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    result = soup.find_all('ol', class_='list_popcmt')
    result2 = result[1].find_all('a')
    for idx in range(len(result2)):
        ts = result2[idx]
        ts = ts.text.replace('\n', '')
        ts = ts.replace('  ', '')
        msg += ts+'\n'
    lbl_result.config(text=msg)


win = Tk()
win.geometry('500x300')
win.title("뉴스")

lbl_tit = Label(win, text='댓글 많은 뉴스')
btn_get = Button(win, text='뉴스 보기', command = fr)
lbl_result = Label(win, text='')


lbl_tit.pack()
btn_get.pack(pady = 5)
lbl_result.pack()

win.mainloop()