# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 19:01:13 2020

@author: Kapil
"""
salary='$876,001'
print(salary)
l1=salary.split('$')
print(l1)
s2="".join(l1)
print(s2)
l2=s2.split(',')
print(l2)
s3="".join(l2)
print("Salary= ",s3)
salary1=int(s3)
print("salary= ",salary1)
print(type(salary1))


#Version 2
salary="$876,001"
salary=int("".join(salary[1:].split(",")))
print(salary)
