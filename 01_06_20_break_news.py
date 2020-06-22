# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:24:48 2020

@author: marco
"""
#Here's one way you could do this.

headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
#print(type(news_ticker))
for headline in headlines:
    news_ticker += headline + " "
#    print(news_ticker)
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        #print(news_ticker)
        break

print(news_ticker)
print(type(news_ticker))

