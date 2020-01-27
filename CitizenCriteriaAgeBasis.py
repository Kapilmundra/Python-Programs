# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:42:17 2020

@author: Kapil
"""

age=int(input("Enter the age= "))
if(age==0 or age==1):
    print("Infant")
elif(age>1 and age<18):
    print("Child")
elif(age>=18 and age<60):
    print("Adult")
else:
    print("Senior Citizen")
