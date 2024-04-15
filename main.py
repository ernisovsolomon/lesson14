import requests

from bs4 import BeautifulSoup

response = requests.get('https://globus-online.kg/')

soup = BeautifulSoup(response.text, 'html.parses')
print()