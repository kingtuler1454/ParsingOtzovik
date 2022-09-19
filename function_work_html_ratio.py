import requests
import info
import page_opinions
import os
from bs4 import BeautifulSoup
def function_work_html_ratio(i):
    if not os.path.isdir("dataset"):
        os.makedirs("dataset/"+str(i))
    html_text = requests.get(info.base_URL+'/?ratio='+str(i), headers={"User-Agent": info.user_agent}).text
    soup = BeautifulSoup(html_text, 'lxml')

    info_max_page=soup.find('a',class_='pager-item last tooltip-top', href=True) # находим кнопку посследней макс страницы
    info_max_page=info_max_page['href']
    slash=info_max_page.split('/')
        #slash[3] - номер макс страницы
    for j in range (1): # slash[3]
        page_opinions(j,i)
