import requests
from bs4 import BeautifulSoup
from tkinter import *


def tran():
    a = ent_word.get()
    msg = a+' 결과\n\n'
    url = 'https://dic.daum.net/search.do?q=' + a
    respan = requests.get(url)
    soup = BeautifulSoup(respan.text, 'html.parser')
    soup2 = soup.find('div', class_='cleanword_type kuek_type')
    result = soup2.find_all('li')
    for one in result:
        msg += one.text+'\n'
    lbl_result.config(text=msg)
    ent_word.delete(0, END)


win = Tk()
win.geometry('300x200')
win.title('단어 검색')

lbl_msg = Label(win, text='단어번역기', font=('', 15))
ent_word = Entry(win)
btn_trans = Button(win, text='번역하기', command=tran)
lbl_result = Label(win, text='')

lbl_msg.pack(pady=5)
ent_word.pack()
btn_trans.pack(pady=5)
lbl_result.pack()

win.mainloop()