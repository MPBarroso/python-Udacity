# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 20:44:32 2020

@author: marco
"""


# write your function here
def readable_timedelta1(days):
    return (int(days/7))
def readable_timedelta2(days):
    return (days-int(days/7)*7)
number = 10
test_1 =readable_timedelta1(number)
test_2 = readable_timedelta2(number)
# test your function
  
print("{} week(s) and {} day(s).".format(test_1,test_2))

def readable_timedelta(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
print(readable_timedelta(10))

print(100%7)