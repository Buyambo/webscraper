import urllib.request
import re

# The URL of the Amazon page to scrape
url = 'https://www.amazon.com/s?k=desktop+monitors&ref=nb_sb_noss_1'

# Send a request to the URL and get the HTML response
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

# Use regular expressions to extract the monitor name, price, and rating
pattern = r'<span class="a-text-normal">(.*?)</span>.*?<span class="a-offscreen">(.*?)</span>.*?<span class="a-icon-alt">(.*?) out of 5 stars</span>'
matches = re.findall(pattern, html)

# Loop through each match and print out the monitor name, price, and rating
for match in matches:
    name = match[0]
    price = match[1]
    rating = match[2]
    
    # Print out the results
    print('Name:', name)
    print('Price:', price)
    print('Rating:', rating)
    print('\n')
