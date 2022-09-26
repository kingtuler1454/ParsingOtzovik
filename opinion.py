import requests
from bs4 import BeautifulSoup

import info
import page_opinions
import get_site


def opinion(i, j, href, number_opinion):
    soup = get_site.get_site(href,'https://otzovik.com/')
    plus = soup.find(class_ = 'review-plus')  # находим достоинство
    minus = soup.find(class_ = 'review-minus')  # находим негатив
    opinion = soup.find(class_='description')  # находим отзыв
    namefile = str(number_opinion).zfill(4)
    text = ''
    text = 'Достоинства:\n' + plus.text + '\n'+'Недостатки:\n' + minus.text + '\n' + 'Отзыв:\n'+ opinion.text
    with open('dataset/' + str(i) + '/' + namefile + '.txt', 'w+') as file:
        file.write(text) 
    print( f'Звезда {str(i)} отзыв {namefile} создан')
   