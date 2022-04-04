from attr import s
from bs4 import BeautifulSoup
import requests 
import smtplib 
import time 
import datetime 

#connect to the website 

URL = "https://www.amazon.in/Acer-HA220Q-21-5-inch-Ultra-Monitor/dp/B07JDH2C8X/ref=zg_bs_1375425031_1/261-8757700-6063309?pd_rd_i=B07JDH2C8X&th=1"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, 'html.parser')

soup2 = BeautifulSoup(soup1.prettify(),"html.parser")

title = soup2.find(id="productTitle").get_text()

# print(title)

price = soup2.find(id="corePrice_desktop").get_text()

# print(price)

# print(price.strip()[1:])
# title = title.strip()
# print(title)
# print(type(price))
import csv 
today = datetime.date.today()

header = ['Title', 'Price', 'Date']
data = [title,price, today]

with open('amazonwebscraper.csv','w', newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)




today = datetime.date.today()

print(today)