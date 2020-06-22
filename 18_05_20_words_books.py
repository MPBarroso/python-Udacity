# -*- coding: utf-8 -*-
"""
Created on Mon May 18 19:28:16 2020

@author: marco
"""
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
print(word_counter)

#for word in book_title:
#    word_counter[word] = word_counter.get(word, 0) + 1 
#print(word_counter)       
