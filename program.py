from bs4 import BeautifulSoup
import requests
from pandas import DataFrame

html_response = requests.get(url="https://coinmarketcap.com/")
soup = BeautifulSoup(html_response.text, "html.parser")
names_html = soup.find_all("p", attrs={"class": "sc-65e7f566-0 iPbTJf coin-item-name"})
prices_html = soup.find_all("div", attrs={"class": "sc-142c02c-0 lmjbLF"})


names = []
prices = []
day = []
for i in range(10):
    names.append(names_html[i].text)
    prices.append(prices_html[i].text)

data = DataFrame({"Currency": names, "Price": prices})
print(data)