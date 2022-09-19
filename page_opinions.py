import requests
import info.py
from bs4 import BeautifulSoup

def page_opinions(j,i):

    html_text=requests.get(info.base_URL+'/'+str(j)+'/?ratio='+str(i), headers={"User-Agent": info.user_agent}).text

    soup = BeautifulSoup(html_text, 'lxml')
    page_opinion=soup.find('a',class_='review-btn review-read-link', href=True) # находим кнопку посследней макс страницы
    print(page_opinion)
    #review-btn review-read-link
