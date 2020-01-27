# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 17:40:51 2020

@author: Kapil
"""

print("Book Shop\n")
orders=[["34587","Learning Python,Mark Lutz",4,40.95],["98762","Programing python, Mark Lutz",5,56.80],["77226","Head first Python,Paul Barry",3,32.95],["88112","Einfuhrung in Python3, Bernd klein",3,24.99]]
print(orders)
print("\nBefore applying Extra charges of rs 10 on less then 100 total amount ")
print("Order No , Price of Total Quantity")
list1=[(item[0],item[2]*item[3]) for item in orders]
print(list1)
def f2(x):
    if(x<100):
        return x+10
    else:
        return x
print("\nAfter applying Extra charges of rs 10 on less then 100 total amount ")
print("Order No , Price of Total Quantity")
list2=[(item[0],f2(item[2]*item[3])) for item in orders]
print(list2)

