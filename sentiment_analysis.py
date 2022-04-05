#sentiment analysis without vector conversion 
#the accuracy is questionable 
#the script uses various libraries to prase the data 

from textblob import TextBlob
from newspaper import Article 

url = "https://www.hindustantimes.com/bollywood/kabir-singh-movie-review-shahid-kapoor-plays-the-fool-in-this-toxic-troubling-film/story-rBQXfpOZmcFDqRSHIlVrXM.html"
article = Article(url)

article.download()    #download to get it into script
article.parse()       #parse to remove all the unusual items and to make it more readable 
article.nlp()         #basically preparing the article for natural language processing 


text = article.text
#print(text)


blob = TextBlob(text)

sentiment = blob.sentiment.polarity #-1 to 1

print(sentiment)