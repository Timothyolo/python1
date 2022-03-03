#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - strings test true"""

a=input("Enter the value of a = ")
b=input("Enter the value of b = ")
c=input("Enter the value of c = ")

if(a>b and a>c):
    print("a is greater")
elif(b>a and b>c):
    print("b is greater")
elif(c>a and c>b):
    print("C is greater")
else:
    print("all numbers are same")



