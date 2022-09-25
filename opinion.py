import requests
import info
import page_opinions
from bs4 import BeautifulSoup
import time

def opinion(i,j, href,number_opinion):
    time.sleep(60)  
    html_text=requests.get('https://otzovik.com/'+href, headers={"User-Agent": info.user_agent},proxies=info.proxies).text
    soup = BeautifulSoup(html_text, 'lxml')
    plus=soup.find(class_='review-plus') # находим достоинство
    minus=soup.find(class_='review-minus') # находим негатив
    opinion=soup.find(class_='description') # находим отзыв
    if number_opinion>=3: # 1
        namefile='0'+str(number_opinion)
    elif number_opinion>=2:
        namefile='00'+str(number_opinion)
    elif number_opinion>=1:
        namefile='000'+str(number_opinion)
    else:
        namefile="0000"+str(number_opinion)
    text=''
    text='Достоинства:\n'+plus.text+'\n'+'Недостатки:\n'+minus.text+'\n'+'Отзыв:\n'+ opinion.text
    with open('dataset/'+str(i)+'/'+namefile+'.txt', 'w+') as file:
        file.write(text) 
    print('Звезда '+str(i)+' отзыв '+namefile+' создан')
