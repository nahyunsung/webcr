from tkinter import *
import requests
from bs4 import BeautifulSoup


def fr():
    url = 'https://news.daum.net/'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    result = soup.find_all('ol', class_='list_popcmt')[0]
    result2 = result.find_all('a')
    for x in range(len(result2)):
        rs = result2[x]
        rs = rs.text.replace('\n', '')
        rs = rs.replace('  ', '')
        lst_news.insert(END, rs)
        ad.append(result.a['href'])
    print(ad)


win = Tk()
win.geometry('500x200')
win.title('뉴스')

ad = []

lbl_tit = Label(win, text='열독률 높은 뉴스')
btn_get = Button(win, text='뉴스 보기', command = fr)
lst_news = Listbox(win, width = 60)

lbl_tit.pack()
btn_get.pack(pady=5)
lst_news.pack()

win.mainloop()