# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 17:36:37 2020

@author: Kapil
"""

saleries=["$876,001","$543,903","$2453,896"]
list1=[]
for item in saleries:
    item1=int("".join(item[1:].split(",")))
    list1.append(item1)
print(list1)
