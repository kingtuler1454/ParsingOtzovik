import requests
from bs4 import BeautifulSoup
import time

"""list=soup.find_all(class_ ="review-title", itemprop="name")
element =list[0]

url= "https://otzovik.com/"+element.get('href')
html_text = requests.get(URL, headers={"User-Agent": user_agent}).text
soup = BeautifulSoup(html_text, 'lxml')

list1=soup.find()
"""


def main():
    #'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    #html_text = requests.get(URL, headers={"User-Agent": user_agent}).text
    #soup = BeautifulSoup(html_text, 'lxml')
    #print(html_text)
    #block_of_ratios=soup.find('div',href=True)
    #print(block_of_ratios)
    #ratios=block_of_ratios.find_all(href=True)
    #print(ratios)

    for i in range (1,2): # для каждой звезды
        #time.sleep(1000)
        

        html_text = requests.get(base_URL+'/?ratio='+str(i), headers={"User-Agent": user_agent},proxies=proxy).text
        soup = BeautifulSoup(html_text, 'lxml')
        info_max_page=soup.find('a',class_='pager-item last tooltip-top', href=True)
        print(soup)
        info_max_page=info_max_page['href']
        slash=info_max_page.split('/')
        print(slash[3])
        for j in range (1): # slash[3]
            time.sleep(1000)
            html_text=requests.get(base_URL+'/'+str(j)+'/?ratio='+str(i), headers={"User-Agent": user_agent}).text
            soup = BeautifulSoup(html_text, 'lxml')
            info_otziv=soup.find_all(class_ ="review-title", itemprop="name")
            print(info_otziv)


if __name__=='__main__':
    main()
