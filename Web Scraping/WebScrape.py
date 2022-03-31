import requests
from bs4 import BeautifulSoup

#lxml is a Python library which allows for easy handling of XML and HTML files,
#  and can also be used for web scraping.
url='https://quotes.toscrape.com/'

response=requests.get(url)
soup=BeautifulSoup(response.text,'lxml')
quotes=soup.find_all('span', class_='text')
authors=soup.find_all('small',class_='author')
tags=soup.find_all('div',class_='tags')
for i in range(0,len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quotesTag=tags[i].find_all('a',class_='tag')
    for qT in quotesTag:
        print(qT.text)
