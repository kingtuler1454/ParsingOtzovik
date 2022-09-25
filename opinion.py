import requests
import info
import page_opinions
from bs4 import BeautifulSoup
import time

def opinion(i,j, href):
    time.sleep(2)  
    html_text=requests.get('https://otzovik.com/'+href, headers={"User-Agent": info.user_agent}).text
    soup = BeautifulSoup(html_text, 'lxml')
    plus=soup.find(class_='review-plus') # находим достоинство
    minus=soup.find(class_='review-minus') # находим негатив
    opinion=soup.find(class_='description') # находим отзыв
    if len(str(j))>=3: # 1
        namefile='0'+str(j)
    elif len(str(j))>=2:
        namefile='00'+str(j)
    elif len(str(j))>=1:
        namefile='000'+str(j)
    else:
        namefile="0000"+str(j)
    text=''
    text='Достоинства:\n'+plus.text+'\n'+'Недостатки:\n'+minus.text+'\n'+'Отзыв:\n'+ opinion.text
    with open('dataset/'+str(i)+'/'+namefile+'.txt', 'w+') as file:
        file.write(text) 
    print('Звезда '+str(i)+' отзыв '+namefile+' создан')