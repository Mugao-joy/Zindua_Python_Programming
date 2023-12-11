#requests module is for sending http requests in python
import requests
from bs4 import BeautifulSoup

url = 'https://zinduaschool.com/blog/'

response = requests.get(url)
#print(response.status_code)

content = response.text
#print (response.text)

soup = BeautifulSoup(content, 'html.parser')
#html.parser breaks down a html doc into constituent parts and to a representation known as DOM; document object model

with open('index.html', mode = 'w') as html_file:
    html_file.write(soup.prettify())

container = soup.find('div', class_ = 'entry-title')
articles = container.find('header', class_ = 'entry-header')

with open('content.txt', mode = 'w')as file:
    for article in articles:
        titles = article.find('h2', class_ = 'entry-title')
        authors = article.find('span', class_ = 'author')
        print(f'Title: {titles.text}\nAuthor: {authors.text}\n')