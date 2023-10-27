from bs4 import BeautifulSoup
import lxml
import requests

url = "https://en.wikipedia.org/wiki/List_of_online_payment_service_providers"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

table = soup.select("tbody")
singapore = table[0]
print(singapore)