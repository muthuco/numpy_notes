#!/usr/bin/env python
# coding: utf-8

# In[2]:


## 1.Write Python Program which take one number as input and find factorial and print the factorial.
### Example:
### Enter the number 3
### Factorial 6

x=int(input("Please enter the number to find factorial for: "))
f=1
  
if(x<0):
    print("Sorry, Factorial does not exist for negative numbers")
elif(x>=0):
    for i in range(1,x+1):
        if(i<=x):
            f=f*i
    print("ANSWER : Factorial of",i, "is",f)     


# In[3]:


#2.Write a python Program which take input from user and find simple intrest.

p=int(input("Enter the principal amount "))
n=int(input("Enter the number of time unit "))
r=int(input("Enter the rate of interest "))

si=p*n*r/100
print("Simple interest for the given parameters is", si)


# In[14]:


#3.Python Program for Fibonacci numbers.

n = int(input("Enter the Fibanacci number's position :"))
f1,f2,fib = (0,1,0)
if(n<=0):
    print("Sorry, you can't enter negative numbers or zero")
else:
    for i in range(1,n+1):
        fib = f1
        newf2 = f1+f2
        # update new values
        f1 = f2
        f2 = newf2
        #print(fib, end = " ")
    print(fib)  


# In[18]:


# 4.Python Program for How to check if a given number is Fibonacci number?

import math

n = int(input("Enter number to verify if Fibonacci number "))
x = 5*pow(n,2)+4 
y = 5*pow(n,2)-4

a = math.sqrt(x)
b = math.sqrt(y)

if((int(a+0.5)**2==x) or (int(b+0.5)**2==y)):
    print(n," is a Fibonacci number")
else:
    print(n," is not a Fibonacci number")


# In[21]:


#5.Python Program for Sum of squares of first n natural numbers
n = int(input("Enter the number of square of natural numbers to be added"))
s = 0

for i in range(1,n+1):
    s=s+pow(i,3)

print("Sum of square of first ",n, " natural numbers is ", s)


# In[ ]:




