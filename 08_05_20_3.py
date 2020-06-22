# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:55:33 2020

@author: marco
"""

#animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}
#print(animals['fish'])
# invalid dictionary - this should break
#room_numbers = {403 :['Freddie', 'Jen'],411:['Ned', 'Keith'],395:['Eugene', 'Zach']}
#print(room_numbers)

room_numbers = {
    ('Freddie', 'Jen'): 403,
    ('Ned', 'Keith'): 391,
    ('Kristin', 'Jazzmyne'): 411,
  ('Eugene', 'Zach'): 395}
print(room_numbers)