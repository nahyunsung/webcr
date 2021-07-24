from tkinter import *
import requests
from bs4 import BeautifulSoup

win = Tk()
win.geometry("500x300")
win.title('뉴스보기')

url = 'https://news.daum.net/'
soup = requests.get(url)
respan = BeautifulSoup(soup.text, 'html.parser')

result1 = respan.find_all('ol', class_='list_popcmt')[1]
result2 = result1.find_all('a')
print(result2)
for one in range(len(result2)):
    result = result2[one]
    result = result.text.replace('\n', '')
    result = result.replace('  ', '')
    print(result2[one])
    link = result2[one]['href']
    print(result)


win.mainloop()