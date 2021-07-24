from tkinter import *
import requests
from bs4 import BeautifulSoup

win = Tk()
win.geometry("500x300")
win.title("뉴스")

lst_box = Listbox(win, width = 80)

url = 'https://news.naver.com/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
soup = requests.get(url, headers=headers)
respan = BeautifulSoup(soup.text, 'html.parser')

title = respan.find('a', class_='nclicks(sci.title)')
result = respan.find_all('ul', class_='mlist2 no_bg')
result2 = result[5].find_all('a')

print(title.text)
for one in result2:
    lst_box.insert(END, one.text)
    print(one.text)


lst_box.pack()


win.mainloop()
