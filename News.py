import requests
import json
queue = input("Enter which news you are intersted in : ")
r = requests.get(f"https://newsapi.org/v2/everything?q={queue}&from=2025-01-20&sortBy=publishedAt&apiKey=65287c2a763f490bb45e92a67bb36341")
news = json.loads(r.text)

# print(news)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")