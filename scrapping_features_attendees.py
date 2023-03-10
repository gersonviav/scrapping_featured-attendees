from turtle import position
from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get("https://www.cloudfest.com/featured-attendees")
soup = BeautifulSoup(page.content, 'html.parser')
# seven_day = soup.find(id="content")
div = soup.find('div', attrs={'class':'cfs-attendees-grid-container'})
div_body = div.find_all('div',attrs={'class':'cfs-attendees-grid-item__content'})

print(div_body[0])
# table_body = table.find('tbody')
# rows = table_body.find_all('tr')
# print(rows)
# for row in rows:
nombres  = []
company = []
position = []
for d in div_body:
    names = d.find_all('h3')
    # print(names)
    names =  [ele.text for ele in names]
    print(names[0])
    nombres.append(names[0])

    company_position = d.find_all('p')
    # print(company_position)
    company_position =  [ele.text for ele in company_position]
    print(company_position)
    company.append(company_position[0])
    position.append(company_position[1])

print(company,position)
df_company_position= pd.DataFrame({
    "Names": nombres,
    "Company": company,
    "Position": position
})
print(df_company_position.head(40))