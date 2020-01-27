# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:31:52 2020

@author: Kapil
"""
print("Welcome to the Shopping list app")
list1=[]
a=1
while(a):
    print("1. Add item in list")
    print("2. Print list")
    print("3. Remove item from the list")
    print("4. Exit From the app")
    b=int(input("Enter your choise="))
    c=1
    while(c):
        if(b==1):
            list1.append(input("Enter the name of your item="))
            c=0
        if(b==2):
            print(list1)
            c=0
        if(b==3):
            list1.remove(input("Enter the name of Remove item from the list="))
            c=0
        if(b==4):
            a=0
            c=0
            
