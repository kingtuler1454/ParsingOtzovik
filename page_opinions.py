import requests
import info
import opinion
from bs4 import BeautifulSoup
import time

def page_opinions(j ,i,number_opinion):
    print("Мы на странице "+str(j)+' звезды '+str(i))
    time.sleep(30)  
    html_text=requests.get(info.base_URL+'/'+str(j)+'/?ratio='+str(i), headers={"User-Agent": info.user_agent},proxies=info.proxies).text
    soup = BeautifulSoup(html_text, 'lxml')
    page_opinion=soup.find_all('a',class_='review-btn review-read-link', href=True) # находим кнопку  ссылок
    for element in page_opinion: # для каждого элемента будем сплитом делить и находить ссылку href
        spisok=str(element).split('"') # spisok[3] это ссылка
        opinion.opinion(i,j,spisok[3],number_opinion)
