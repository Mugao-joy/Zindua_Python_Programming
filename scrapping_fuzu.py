import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('jobs.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS jobs')
cursor.execute('CREATE TABLE jobs(Company, Title, Location, Deadline)')

response = requests.get('https://www.fuzu.com/job')
#print(response.status_code)
content = response.text
#print(content)

soup = BeautifulSoup(content , 'html.parser')
#print(soup.prettify)

with open('index.html', mode = 'w') as html_file:
    html_file.write(soup.prettify())
    
container = soup.find('section', class_ = 'job-list')
jobs = soup.findAll('a', class_ = 'clickable')

with open('jobs.txt', mode = 'w') as file:
    for job in jobs:
        company = job.find('p', class_ = 'MDWeZ')
        title = job.find('h2', class_ = 'hXurjM')
        location = job.find('h2', class_ = 'hXurjM')
        remaining_days = job.find('p', class_ = 'bpWsQZ')
        file.write(f'Company: {company.text}\nTitle: {title.text}\nLocation: {location.text}\nDeadline: {remaining_days.text}\n\n')
        cursor.execute('INSERT INTO jobs VALUES(?,?,?,?)', (company.text, title.text, location.text, remaining_days.text))
        conn.commit()

cursor.close()
print(conn)
        
#print(jobs)
#print(container)
#job title
#location
#company name
#deadline