#!/usr/bin/env python
# coding: utf-8

# # Python using Jupyter Practice

# This is a notebook to practice the knowledge acquired in Jupyter

# ## Basic Exercises

# ### Exercise 1: Calculate the multiplication and sum of two numbers

# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

# In[2]:


number1 = 20
number2 = 30


# In[3]:


print(number1 + number2)


# In[4]:


number3 = 40
number4 = 30


# In[5]:


print(number3 + number4)


# ### Exercise 2: Print the sum of the current number and the previous number

# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

# In[8]:


var= 0
for i in range(1,10+1):
    sum = var + i
    print(f"Current number: {i}, Previous number: {var}, Sum number: {sum}")
    var = i


# ### Exercise 3: Print characters from a string that are present at an even index number

# Write a program to accept a string from the user and display characters that are present at an even index number.
# 
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

# In[21]:


string_=input("Type a word ")
array_= list(string_)
for i in range (1,len(string_),2):
    print(array_[i])

    


# ### Exercise 4: Remove first n characters from a string

# Write a program to remove characters from a string starting from zero up to n and return a new string.
# 
# For example:
# 
# * remove_chars("pynative", 4) so output must be tive. Here, we need to remove the first four characters from a string.
# * remove_chars("pynative", 2) so output must be native. Here, we need to remove the first two characters from a string.
# 
# Note: n must be less than the length of the string.

# In[35]:


word= input("Type the word you wanna slice ")
n=input(f"The length of your word is {len(word)} , type the number of characters that you wanna remove ")
new_word = word[int(n):]
print(f"Your new word is {new_word}")

    


# ### Exercise 5: Check if the first and last number of a list is the same

# Write a function to return True if the first and last number of a given list is same. 
# If numbers are different then return False.

# In[57]:


def list_(a):
    
    first=a[0]
    last=a[-1]

    if first == last:
        return True

    else:
        return False
    
x=list_([1,2,3,4])
y=list_([1,2,3,1])

print(x , y)


# ### Exercise 6: Display numbers divisible by 5 from a list

# Iterate the given list of numbers and print only those numbers which are divisible by 5

# In[60]:


def list_div(list_):
    print(f"{list_} \n")
    for i in list_:
        if i % 5 == 0:
            print(i)
            
list_div([1,5,6,10,11,15,16,20,21,26])
    


# ### Exercise 7: Return the count of a given substring from a string

# Write a program to find how many times substring “Emma” appears in the given string.
# 
# Given: "Emma is good developer. Emma is a writer"
# 

# In[61]:


def count_substring(string):
    count=string.count("Emma")
    return f"the word Emma appears {count} times"

count_substring("Emma is good developer. Emma is a writer")


# ### Exercise 8: Print the following pattern

# * 1 
# * 2 2 
# * 3 3 3 
# * 4 4 4 4 
# * 5 5 5 5 5

# In[82]:


def pyramid(num):
    for n in range(num+1):
        for i in range(n):
            print (n, end=" ") 
        print("\n")

pyramid(5)
            
            


# ### Exercise 9: Check Palindrome Number

# Write a program to check if the given number is a palindrome number.
# 
# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

# In[95]:


def palindrome(a):
    a_string=str(a)
    a_list=list(a_string)
    a_list_reverse=a_list[::-1]
    reverse= "".join(a_list_reverse)
    b= int(reverse)
    
    if a == b:
        print(f"{a} is a palindrome")
    else:
        print(f"{a} is not a palindrome")

palindrome(545)
palindrome(542)
palindrome(145)
palindrome(242)



    


# ### Exercise 10: Create a new list from two list using the following condition

# reate a new list from two list using the following condition
# 
# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

# In[103]:


def mixing_lists(a,b):
    new_list=[]
    for i in (a):
        if i % 2 == 0:
            new_list.append(i)
            
    for j in (b):
        if j % 2 != 0:
            new_list.append(j)    
            
    return new_list
    

mixing_lists([1,2,3,4,5],[6,7,8,9,10])


# ### Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

# In[104]:


def reverse_number(number):
    number_into_string=str(number)
    str_into_list=list(number_into_string)
    reverse_str=str_into_list[::-1]
    joined_str=" ".join(reverse_str)
    return joined_str

reverse_number(543019)


# ### Ejercicio 12: Calcule el impuesto sobre la renta para los ingresos determinados siguiendo las reglas siguientes

# In[128]:


#+---------------+------------+
#|Tacable income | Rate(in %) |
#+---------------+------------+
#|First $10,00   | 0          |
#|Next $10,00    | 10         |
#|The remaining  | 20         |
#+---------------+------------+


# For example, suppose the taxable income is 45000, and the income tax payable is
# 
# 10000*0% + 10000*10%  + 25000*20% = $6000

# In[119]:


def income(money):
    tax= 0
    
    if money <= 10000:
        tax = 0

        
    elif money <= 20000:
        x = money - 10000
        tax = x * 10 / 100
        
    else:
        tax = 0
        tax = 10000 * 10 / 100
        tax += (money - 20000) * 20 / 100
        
    return tax

income(45000)


# ### Exercise 13: Print multiplication table from 1 to 10

# In[127]:


for num in range(1,10+1):
    for mult in range(1,10+1):
        print(num*mult,end="-")
    print("\n")


# ### Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)

# In[129]:


# * * * * *  
# * * * *  
# * * *  
# * *  
# *


# In[133]:


for i in range(6,0,-1):
    for j in range (0,i-1):
        print("*",end=" ")
    print('\n')


# ### Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

# Note here exp is a non-negative integer, and the base is an integer.

# In[1]:


def exponent(b,e):
    while b > 0 and e > 0:
        return b**e


exponent(5,4)


# ## Intermediate Exercises

# ### Exercise 1: Reverse each word of a string

# Given str = 'My Name is Jessa' Expect yM emaN si asseJ

# In[20]:


def reverse_str(str):
    split_string=str.split()

    new_list=[]

    for word in split_string:
        new_word=word[::-1]
        new_list.append(new_word)

    new_str= " ".join(new_list)
    return new_str
    
    
    

reverse_str("My Name is Jessa")
    


# ### Exercise 2: Read text file into a variable and replace all newlines with space

# In[19]:


#Given: Assume you have a following text file (sample.txt).

#Line1
#line2
#line3
#line4
#line5


# In[21]:


# Line1 line2 line3 line4 line5


# In[31]:


import os

with open('C:\\Users\\ro_be\\Desktop\\sample.txt', 'r') as file:
    data = file.read().replace('\n', ' ')
    print(data)


# In[ ]:




