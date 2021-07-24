from tkinter import *
import requests
from bs4 import BeautifulSoup

def find():
    lst_box.delete(0, END)
    titles.clear()
    links.clear()
    url = 'https://news.naver.com/'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    soup = requests.get(url, headers=headers)
    span = BeautifulSoup(soup.text, 'html.parser')

    sec = span.find('div', id='section_it')
    title = sec.find('h4').text
    lab_title.config(text=title)
    news_bk = sec.find('ul', class_='mlist2 no_bg')
    news = news_bk.find_all('li')
    for one in news:
        lst_box.insert(END, one.text)
        title = one.a.text.strip()
        link = one.a['href']
        titles.append(title)
        links.append(link)
        print(title, link)
    print(titles)

win = Tk()
win.geometry('500x300')
win.title('뉴스')

titles = []
links = []

lab_title = Label(win, text='')
lst_box = Listbox(win, width='50')
but_news = Button(win, text='뉴스 업데이트', command=find)

find()

lab_title.pack()
lst_box.pack()
but_news.pack()


win.mainloop()