# Have Beautiful Soup installed by running pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

# The URL of the Amazon page to scrape
url = 'https://www.amazon.com/s?k=desktop+monitors&ref=nb_sb_noss_1'

# Send a request to the URL and get the HTML response
response = requests.get(url)
html = response.content

# Use Beautiful Soup to parse the HTML response
soup = BeautifulSoup(html, 'html.parser')

# Find all the div elements with the class "s-result-item"
monitor_divs = soup.find_all('div', {'class': 's-result-item'})

# Loop through each div element and extract the monitor name, price, and rating
for div in monitor_divs:
    name = div.find('span', {'class': 'a-text-normal'}).text
    price = div.find('span', {'class': 'a-offscreen'}).text
    rating = div.find('span', {'class': 'a-icon-alt'}).text
    
    # Print out the results
    print('Name:', name)
    print('Price:', price)
    print('Rating:', rating)
    print('\n')
