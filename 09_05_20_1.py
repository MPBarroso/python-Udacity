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
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True
print(elements)