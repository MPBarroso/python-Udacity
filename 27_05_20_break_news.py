# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:16:12 2020

@author: marco
"""
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

ticker = ""

for letter in headlines:
    if len(ticker) >= 140:
        print("It's done")
        ticker = ticker[:140]
        break
    ticker += letter + " "
    
print(len(ticker))
print(ticker)

#    else:
#        head_2[letter]=head_1[letter].append()
#        print(head_2)
#print(len(head_2))
    
#while len(head_2) <= 140:  
#print(len(head_1))
#test_0 = {}
#for i in headlines:
#    test_0.append(i)
#    headlines[0].count()
#    print(test_0)#test_0[i] = headlines[i].split()
   # print(test_0)

#print(test_0)


#print(range(len(headlines)))