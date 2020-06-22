# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:25:02 2020
@author: marco
"""
# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
#elements = {'hydrogen':{'number':1,'weight':1.00794,'symbol':'H','is_noble_gas':False},
           # 'helium':{'number': 2, 'weight': 4.002602, 'symbol': 'He','is_noble_gas':True}}
#print(max(elements))
#print(elements['helium']['is_noble_gas'])
#elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            #'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
#elements['hydrogen']['is_noble_gas'] = False
#elements['helium']['is_noble_gas'] = True
#print(elements)
verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
#print(verse, '\n')
list_1=verse.split()
print('This is the list:',list_1)
print('This is the length of list:', len(list_1))
set_1=set(list_1)
print('This is the set', set_1)
print('Thiis is the length of set', len(set_1))
 