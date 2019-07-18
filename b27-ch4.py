#!/usr/bin/env python
# coding: utf-8

# # Chapter 4

# In[ ]:


my_var = 3
print(type(my_var))
my_var = "foo"
print(type(my_var))
my_var = len  # Even a function!
print(type(my_var))


# In[ ]:


my_var = 'foo\nbar'   # \n means newline
print("1:", my_var)
my_var = "foo\nbar"
print("2:", my_var)
my_var = """foo

bar"""
print("3:", my_var)


# In[ ]:


my_string = str(123)
my_int = int(my_string)
almost_pi = float("3.14159")


# In[ ]:


import random
random.randrange(20, 30)


# In[ ]:


for i in range(0, 10):
    print(i)


# In[ ]:


for color in ["red", "green", "blue"]:
    print(color)


# In[ ]:


for i in range(3):
    print("repeated")
    print("also repeated")
print("not repeated")


# In[ ]:


my_list = ["string", 1, [2.0, 4.5], 5.6]  # Don't do that
print(my_list)
my_list = []                              # An empty list
print(my_list)
my_list = [3, 4, 6, 2, 45, 23, 12, 34]    # That's better
print(my_list)


# In[ ]:


my_list[2] = 64
my_list


# In[ ]:


my_list[0]


# In[ ]:


my_list[-2]


# In[ ]:


my_list[0:2]


# In[ ]:


print(len(my_list))
print(min(my_list))
print(max(my_list))
print(sum(my_list))
print(my_list * 2)
my_list.append(146)    # Changes my_list
other_list = my_list + [1, 2, 3]   # Doesn't change my_list, need to store returned value
print(other_list)


# In[ ]:


my_var = "Abc defg hij"
print(len(my_var))
print(max(my_var))        # Why would you do that?
# sum(my_var)      # This doesn't work
# my_var[1] = 'v'  # Nor this
print(my_var[2:6])
print(my_var * 2)


# In[ ]:


print(my_var.lower())
print(my_var.upper())
print(my_var.title())
print(my_var.startswith("Abc"))
print(my_var.endswith("xyz"))
list_of_string = my_var.split(" ")
new_string = "#$#".join(list_of_string)
print(new_string)


# In[ ]:


if sum(my_list) == 333:
    print("It's 333 exactly!")
else:
    print("It's some other value")


# In[ ]:


if my_list[0] > 20 and my_list[1] <= 14 or my_list[2] != 5 and 4 in my_list and 65 not in my_list:
    print("Weird condition")


# In[ ]:


total = 0
for val in my_list:
    if val % 2 == 1:
        total += val
total


# In[ ]:


with open('mydata.txt', 'r') as md:
    for line in md:
        pass # Do something with each line


# In[ ]:


my_dict = {}   # Empty dict
my_dict = {'foo': 'bar', 'baz': 'bak'}
# This one is handy if you have a list of pairs to turn into a dictionary:
my_dict = dict([['foo', 'bar'], ['baz', 'bak']])


# In[ ]:


my_dict['foo']


# In[ ]:


my_dict['hello'] = 'world'
my_dict['hello'] = 'goodbye'


# In[ ]:


for key in my_dict:
    print("The key", key, "maps to the value", my_dict[key])


# In[ ]:


def double_plus_y(x, y=4):
    return 2 * x + y

double_plus_y(6)


# In[ ]:


def say_hi():
    print("Just saying 'hello'.")

say_hi()


# In[ ]:


for value in map(double_plus_y, my_list):
    print(value)


# In[ ]:


for value in map(lambda x: 2 * x, my_list):  # Don't need a separate function
    print(value)


# In[ ]:


[x*2 for x in my_list]


# In[ ]:


[x for x in my_list if x % 2 == 1]


# In[ ]:


cities = ['washington,ct', 'springfield,or', 'riverside,tx', 'franklin,vt', 'lebanon,co', 'dayton,tx', 'las vegas,nm', 'madison,ca', 'georgetown,ct', 'los angeles,tx']
short_cities = []
for city in cities:
    if len(city) < 12:
        short_cities.append(city)
short_cities


# In[ ]:


abbreviations = []
for city in cities:
    abbreviations.append(city[:3])
abbreviations


# In[ ]:


cities = ['washington,ct', 'springfield,or', 'riverside,tx', 'franklin,vt', 'lebanon,co', 'dayton,tx', 'las vegas,nm', 'madison,ca', 'georgetown,ct', 'los angeles,tx']
city_dict = {}
for city in cities:
    splitcity = city.split(",")
    city_dict[splitcity[0]] = [splitcity[1]]
city_dict

