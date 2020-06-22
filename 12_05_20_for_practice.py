# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:24:09 2020

@author: marco
"""
#sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
#for i in sentence:
#    print(i)

#x=range(5,31,5)
#for n in x:
#    print(n)
#print(list(x))
#names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
#usernames=[]
#for name in names:
#    usernames.append(name.lower().replace(' ','_'))
#print(usernames)
#print (name)

 
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for names in range(len(usernames)):
    usernames[names] = usernames[names].lower().replace(" ","_")

print(usernames)

#cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

#for index in range(len(cities)):
#    cities[index] = cities[index].title()
#print(cities)
