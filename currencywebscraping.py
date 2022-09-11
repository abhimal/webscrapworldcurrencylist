import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.currencyremitapp.com/world-currency-symbols/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
table_body = soup.find('tbody')
country = table_body.find_all('tr')
country_list = []
for row in country:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    country_list.append({"country": cols[1], "currency": cols[2], "code": cols[3], "symbol": cols[4]})
print(country_list)
# for data in country_list:
#     print(data)