# -*- coding: utf-8 -*-
"""
Created on Wed May 27 14:57:24 2020

@author: marco
"""
start_num = 0 #provide some start number
end_num =10 #provide some end number that you stop when you hit
count_by = 1 #provide some number to count by 
break_num = 0
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num

while start_num <= end_num:
    break_num +=  1 
    start_num += count_by
#    print(break_num)
#    break_num = break_num*(count_by)
break_num = start_num-count_by+1

print(break_num)
#print("O loop foi realizado {} vezes.".format(break_num))