#importing modules 

from bs4 import BeautifulSoup
import requests 
import pandas as pd 
import csv 

#scraping data 

url = "https://www.flipkart.com/search?q=books"

#get url ani request pass cheyali
r = requests.get(url)

#r.content html.parser 

soup = BeautifulSoup(r.content,"html.parser")

#title, reviews, rating -> muditini scrap cheddam anukunnam 

titles = soup.find_all('a',class_='s1Q9rs')
ratings = soup.find_all('div',class_="_3LWZlK")
prices = soup.find_all('div',class_="_30jeq3")

# print(titles)
t=[]
rat = []
p=[]
# for title in titles:
#     t.append(title.text)

# print(t)

# for rating in ratings:
#     rat.append(rating.text)

# print(rat)

# for price in prices:
#     p.append(price.text)

# print(p)

for title,rating,price in zip(titles,ratings,prices):
    t.append(title.text)
    rat.append(rating.text)
    p.append(price.text)

print(t)
print(rat)
print(p)
# t=[]
# mr=[]
# mp=[]

# for title,rating,pri in zip(titles,ratings,price):
#     t.append(title.text)
#     mr.append(rating.text)
#     mp.append(price.text)



# print(t)

#saving data in csv 
# header_n = ['Title', 'Rating', 'Price']
# data_n = [t,rat,p]
data_dict = {'title':t,'rating':rat,'price':p}
print(data_dict)

# with open('flipcart.csv', 'w', newline='', encoding='UTF8') as f
#     writer = csv.writer(f)
#     # writer.writerow(header)
#     writer.writerows(data_dict)

model = pd.DataFrame(data=data_dict)

model.to_csv("flipkart_data.csv")