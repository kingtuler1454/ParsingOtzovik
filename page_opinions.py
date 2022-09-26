from bs4 import BeautifulSoup

import opinion
import get_site


def page_opinions(j, i, number_opinion):
    print(f'Мы на странице {str(j)} звезды {str(i)}')
    soup = get_site.get_site('/' + str(j) + '/?ratio='+str(i))
    page_opinion = soup.find_all('a', class_='review-btn review-read-link', href=True)  # находим кнопку  ссылок
    for element in page_opinion:  # для каждого элемента будем сплитом делить и находить ссылку href
        spisok = str(element).split('"')  # spisok[3] это ссылка
        opinion.opinion(i, spisok[3], number_opinion)
        number_opinion += 1
    return number_opinion
