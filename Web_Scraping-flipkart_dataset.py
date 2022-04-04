from bs4 import BeautifulSoup 
import requests 
import pandas as pd 
import csv 

url = "https://www.flipkart.com/search?sid=bks&otracker=CLP_Filters&p%5B%5D=facets.language%255B%255D%3DEnglish"

r = requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")

titles = soup.find_all("a", class_="s1Q9rs")
ratings = soup.find_all("div",class_="_3LWZlK")
prices = soup.find_all("div",class_="_30jeq3")

# print(titles)
t = []
# for title in titles: 
#     t.append(title.text)

# print(t)


# print(ratings)

rat = []
# for rating in ratings: 
#     rat.append(rating.text)

# print(rat)


# print(prices)

p = []
# for price in prices: 
#     p.append(price.text)

# print(p)

for title,rating,price in zip(titles,ratings,prices):
    t.append(title.text)
    rat.append(rating.text)
    p.append(price.text)


#store the data in a csv file 

data_dict = {"Title":t,"Rating":rat,"Price":p}

# 

file = pd.DataFrame(data=data_dict)
file.to_csv("youtubev.csv")
