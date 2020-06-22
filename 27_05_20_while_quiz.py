# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:34:46 2020

@author: marco
"""
start_num = 1 #provide some start number
end_num = 10 #provide some end number that you stop when you hit
count_by = 5  #provide some number to count by 
break_num = 0
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
if start_num>=end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."
else:
    while start_num <= end_num:
        break_num +=  1 
        start_num += count_by
        print(break_num)
        result = break_num*count_by+1
#break_num -= 1
print(result)