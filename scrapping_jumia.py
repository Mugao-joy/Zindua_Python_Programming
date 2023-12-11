import requests
from bs4 import BeautifulSoup
import csv
response = requests.get('https://www.jumia.co.ke/')
#print(response.status_code)
content = response.text
soup = BeautifulSoup(content, 'html.parser')

#print(soup.prettify())

top_deals = soup.find('div', class_ = 'crs row _no-g -fw-nw _6cl-4cm -pvxs' ) 
product_names = []
brand_names = []
prices = []
discounts = []
review_counts = []
ratings = []

for deal in top_deals.find_all('div', class_ = 'itm col'):
    product_name = deal.find('div', class_ = 'name').text
    brand= deal.find('div', class_ = 'core')
    #brand_name = brand['data-brand']

    print(brand)
    """price = deal.find('div', class_ = 'prc').text
    discount = deal.find('div', class_ = 'bdg _dsct')
    rating = deal.find('span', class_ = '-m')
    #review_counts = deal.find('div', class_ = 'stars _m _al').text.strip

    product_names.append(product_name)
    #brand_names.append(brand_name)
    prices.append(price)
    discounts.append(discount)
    #review_counts.append(review_counts)
    #ratings.append(rating)"""
    

#print(discounts)
#print(ratings)
"""data_list = []
for i in range(len(product_names)):
    data_list.append({
        'Product Name' : product_names[i], 
        #'Brand Name': brand_names[i],
        'Price (Ksh)': prices[i],
        'Discount (%)': discounts[i],
        #'Total Number of Reviews': review_counts[i],
        #'Product Rating (out of 5)': ratings[i]
    })
    csv_file_name = 'jumia_deals.csv'
    with open (csv_file_name, 'w') as csv_file:
        fieldnames = ['Product Name', 'Brand Name', 'Price (Ksh)', 'Discount (%)', 'Total Number of Reviews', 'Product Rating (out of 5)']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_list)
        print(csv_file)"""