import requests
import info
import page_opinions
import os
from bs4 import BeautifulSoup
import time

def function_work_html_ratio(i):
    for i in range(6):
        os.makedirs("dataset/"+str(i))
    time.sleep(2)  
    html_text = requests.get(info.base_URL+'/?ratio='+str(i), headers={"User-Agent": info.user_agent}).text
    soup = BeautifulSoup(html_text, 'lxml')

    info_max_page=soup.find('a',class_='pager-item last tooltip-top', href=True) # находим кнопку посследней макс страницы
    info_max_page=info_max_page['href']
    slash=info_max_page.split('/')
        #slash[3] - номер макс страницы
    print("Нашли макс количество страниц для звезды: "+str(slash[3]))
    for j in range (int(slash[3])): # slash[3]
        page_opinions.page_opinions(j,i)
