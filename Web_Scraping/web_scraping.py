from bs4 import BeautifulSoup
import requests


url = requests.get('https://www.uol.com.br/').content

soup = BeautifulSoup(url, 'html.parser')

print(soup.prettify())


