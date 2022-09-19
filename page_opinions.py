import requests
import info
import opinion
from bs4 import BeautifulSoup

def page_opinions(j ,i):
    html_text=requests.get(info.base_URL+'/'+str(j)+'/?ratio='+str(i), headers={"User-Agent": info.user_agent}).text
    soup = BeautifulSoup(html_text, 'lxml')
    page_opinion=soup.find_all('a',class_='review-btn review-read-link', href=True) # находим кнопку  ссылок
    for element in page_opinion: # для каждого элемента будем сплитом делить и находить ссылку href
        spisok=str(element).split('"') # spisok[3] это ссылка
        opinion(i,j,spisok[3])
