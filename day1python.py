#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello to the world of python")


# In[4]:


a='10'
a


# In[7]:


# Datatype -> type of the data which is stored inside a variable 
# int-> wholenumber doesn't contain a decimal number
num=10
print(num)
print(type(num))


    


# In[9]:


# float -> decimal number 
num1=354.4
print(num1)
print(type(num1))


# In[12]:


# add 
num2=123
num3=23.45
num4=num2+num3
print(num4)


# In[13]:


# substract 
num1=255
num2=23.86
num3=num1-num2
print(num3)


# In[16]:


# multiply 
num5=2558
num6=263
num7=num5*num6
print(num7)


# In[17]:


# division 
num2=7896
num4=45
num9=num2/num4
print(num9)


# In[18]:


# cancatenation 
num3=5000
num5=2000
print("the multiplication of two values are",(num3*num5))


# In[2]:


name1='teach'
name2='nook'
print(name1,name2)


# In[21]:


x=int(input("enter the value:"))
y=int(input("enter the second value:"))
print("the difference of two values are",(x-y))
print(type(x))
print(type(y))


# In[1]:


# collective datatypes in python
 # list 
 # tuple 
 # set 
 # dictionary    


# In[14]:


# List -> collection of data, ordered, its mutable, []
mylist=["Data","A","Task","Schedule",544,True,245.61]
print("The value of mylist is",mylist)
print(mylist)
print(type(mylist))
# Index value -> print individual data 
print (mylist[0])
print (mylist[1])
print (mylist[2])
print (mylist[3])
print (mylist[4])
print (mylist[5])
print (mylist[6])
print (mylist[-1])
print (mylist[-5])

# changeable 
# updates
mylist[1]="B"
print("The updated values of list is",mylist)


# In[19]:


# Append(add)
mylist.append("details")
print("The values after adding are",mylist)


# In[23]:


# insert 
mylist.insert(3,"insert")
print("The value after indexing is",mylist)


# In[26]:


list1=[1,23,256]

# extend
# mylist.extend(list1)
list1.extend(mylist)
print("The value of list is",mylist)


# In[35]:


# remove
mylist.remove(256)
print("The values are",mylist)


# In[36]:


# remove
mylist.remove("Schedule")
print("The values are",mylist)


# In[37]:


# delete 
del mylist[-6]
print ("The values after deleting is", mylist)


# In[38]:


del mylist
print(mylist)


# In[39]:


list1=[1,2]
list2=[3,4]
list1.extend(list2)
print(list1)


# In[41]:


# tuple -> ordered collection of datatypes, ()
mytuple=("Dell",534,"HP",34.6,False)
print(mytuple)
print(len(mytuple))


# In[1]:


# Dictionary ->{},key and values 
mydic={
    "username":"Admin",
    "Password":"Pass",
    "Batch":2023,
}
print(mydic)


# In[2]:


# Dictionary ->{},key and values 
mydic={
    "username":"Admin",
    "Password":"Pass",
    "Batch":2023,
}
print(mydic)
print(mydic["username"])


# In[3]:


# Dictionary ->{},key and values 
mydic={
    "username":"Admin",
    "Password":"Pass",
    "Batch":2023,
}
print(mydic)
print(mydic["Admin"])


# In[4]:


# Dictionary ->{},key and values 
mydic={
    "username":"Admin",
    "Password":"Pass",
    "Batch":2023,
}
print(mydic)


# Update 
mydic["username"]="Admin123"
print("The values after updating are",mydic)


# In[5]:


# Dictionary ->{},key and values 
mydic={
    "username":"Admin",
    "Password":"Pass",
    "Batch":2023,
}
print(mydic)


# Update 
mydic["Password"]="upadhyayaman"
print("The values after updating are",mydic)


# In[7]:


# We can also have multiple values on key or multiple collection of data on one single keys
# Dictionary ->{},key and values 
mydic={
    "username":"Admin",
    "Password":"Pass",
    "Batch":2023,
}
print(mydic)


# Update 
mydic["Username"]=("Admin123","Owner")
print("The values after updating are",mydic)

#mydic["Course"]="Python"
print("The values are",mydic)

list1=[1,23,34,5]
mydic["Password"]=list1
print("The values are",mydic)


# In[44]:


# Dictionary ->{},key and values 
mydic={
    "username":"Admin",
    "Password":"Pass",
    "Batch":2023,
}
print(mydic)


# Update 
mydic["Username"]=("Admin123","Owner")
print("The values after updating are",mydic)

#mydic["Course"]="Python"
print("The values are",mydic)

list1=[1,23,34,5]
mydic["Password"]=list1
print("The values are",mydic)

mydic.pop("Username")
print("The values are",mydic)

del mydic
print(mydic)







# In[46]:


# Dictionary ->{},key and values 
mydic={
    "username":"Admin",
    "Password":"Pass",
    "Batch":2023,
}
print(mydic)


# Update 
mydic["Username"]=("Admin123","Owner")
print("The values after updating are",mydic)

#mydic["Course"]="Python"
print("The values are",mydic)

list1=[1,23,34,5]
mydic["Password"]=list1
print("The values are",mydic)

mydic.pop("Username")
print("The values are",mydic)

# updating the key 
new=mydic["Course"]
del mydic["Course"]
mydic["Learning"]=new
print(mydic)


# In[24]:


# Set -> unordered collecction of datatypes, {}, doesn't contain a duplicate value 

myset={"data","task",12,354.6,False,12}
print(myset)


# In[33]:


# add 
myset.add("True")
print(myset)


# In[34]:


set1={1,23,4,5,67,8}
set2={2,34,0,56,3}
set3=set1.union(set2)
print(set3)


# In[35]:


Dec={'we':12,'we1':12}
print(Dec)


# In[36]:


set4=set1|set2
print(set4)


# In[37]:


set3=myset|set1
print(set3)


# In[55]:


# Intersection(common)
set3=myset.intersection(set1)
print(set3)

set1={1,23,4,5,67,8}
set2={2,34,0,56,3}
set3=set1&set2
print(set3)


# In[51]:


# Intersection(common)
set1={1,23,4,5,67,8}
set2={2,34,0,56,3}
set3=set1&set2
print(set3)


# In[56]:


set4=set1.difference(set2)
print(set4)



# In[57]:


set2.clear()
print(set2)


# In[3]:


# ASSIGNMENT
# Create a two different example for collective datatypes in python


# In[4]:


# Homework 


# In[5]:


# List example 1 
# List of numbers and strings
numbers_and_strings = [1, 2, 3, "apple", "banana", "cherry"]
print("Example 1 - List:", numbers_and_strings)


# In[8]:


# list example 2 mixed datatypes 
mixed_list = [True, 42, 3.14, "Hello", [1, 2, 3], {"key": "value"}]
print("Example 2 - List:", mixed_list)


# In[10]:


# Tuples example 1
# Tuple of integers
inttuple = (10, 20, 30, 40)
print("Example 1 - Tuple:", inttuple)

# Tuple with mixed data types eg 2
mixedtuple = ("Python", 2024, 3.14, False, [1, 2, 3])
print("Example 2 - Tuple:", mixedtuple)



# In[12]:


# Set of integers eg 1

integerset = {1, 2, 3, 4, 5}
print("Example 1 - Set:", integerset)

# Set with mixed data types (note: sets can only contain immutable elements) eg 2
mixed_set = {"apple", 1, 3.14, (1, 2)}
print("Example 2 - Set:", mixed_set)




# In[16]:


# Dictionary with string keys and integer values eg 1
personinfo = {
    "name": "Alice",
    "age": 30,
    "height": 5.5
}
print("Example 1 - Dictionary:", personinfo)

# Dictionary with mixed types for values
product_info = {
    "product_id": 12345,
    "name": "Laptop",
    "price": 899.99,
    "available": True,
    "tags": ["electronics", "computers"]
}
print("Example 2 - Dictionary:", product_info)



# In[18]:


# Lists: Ordered and mutable collections.
# Tuples: Ordered and immutable collections.
# Sets: Unordered collections of unique items.
# Dictionaries: Collections of key-value pairs.


# In[23]:


print("Hello all \ngood evening \nwelcome back to the class")


# In[87]:


# Function =>A set of data will be executed whenever you call it

def a():
    print("Hello all \ngood evening \nwelcome back to the class")
a()
a()

def name():
    print("Hope you all are doing good")
name()   


# In[88]:


def a():
    for b in range(5):
        print("Hello all \ngood evening everyone \nwelcome back to the class")
a()        
    


# In[89]:


def add(num1,num2):
   print("The addition of two values are",(num1+num2)) 
add()


# In[33]:


def add(num1,num2):
   print("The addition of two values are",(num1+num2)) 
add(2,456)
add(3,454)


# In[56]:


def add1():
    num1=int(input("Enter the first number"))
    num2=int(input("Enter the second number"))
    print("The values are",(num1+num2))
add1()    
    


# In[58]:


def a(name):
    print("My favourite cartoon name is",name)
a("Jacky")


# In[60]:


def multiply1():
    num1=int(input("Enter the first number"))
    num2=int(input("Enter the second number"))
    print("The values after multiplication are",(num1*num2))
multiply1()    


# In[62]:


def minus1():
    num1=int(input("Enter the first number"))
    num2=int(input("Enter the second number"))
    print("The values after substraction are",(num1-num2))
minus1()    


# In[65]:


a=5
for x in range(0,a):
    print(x)


# In[66]:


# we can also substract or multiply directly in the same code 

def add(num1,num2):
   print("The addition of two values are",(num1+num2),"The difference of two values are",(num1-num2)) 
add(2,456)
add(3,454)


# In[67]:


# for loop (printing the data one after the other)


a=5
for x in range(0,a):
    print(x)


# In[70]:


a=10
for x in range(3,a):
    print(x)


# In[73]:


for y in range(10):
    print("The values are",y)


# In[74]:


for y in range(2,20):
    print("The values are",y)


# In[78]:


mylist=["Data","A","Task","Schedule",544,True,245.61]
print(mylist)
for Data in mylist:
    print(Data)


# In[90]:


if(2>6):
    print("The first number is greater")
elif(2<6):
    print("The second number is greater")
else:
    print("The second number is greater")


# In[2]:


if(2>6):
    print("The first number is greater")
elif(2=="2"):
    print("The second number is greater")
else:
    print("None")


# In[3]:


def quiz():
    n = input("Enter your choice (a, b, c, d): ")
    if n in ("a", "b", "d"):
        print("You have lost")
    elif n == "c":
        print("You have won")

quiz()


# In[1]:


for y in range(2,20):
    print("The values are",y)


# In[ ]:





# In[ ]:




