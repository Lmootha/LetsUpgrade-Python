#!/usr/bin/env python
# coding: utf-8

# # Backslash

# In[1]:


print('hi this program       is to check       backslash')


# # Triple Quotes

# In[4]:


print ( """ hello
test program
""")
print(""" This is to use the apostrophe 
it's fun to read
""")


# # Escape Sequence

# In[8]:


print( """ \t \n \''
""")


# # Formatted String

# In[28]:


single_quote = "'"
double_quote = '"'
print ("test %s"%double_quote )
print ("test %s",double_quote )
surround_with_single = "'%s'"
surround_with_double = '"%s"'
print(surround_with_single)
print(surround_with_single % double_quote)


# # Operators, Assignments, Variables

# In[34]:


a = 100
b = 200
c = 300
b+=c
print(a+b)
print(b)
print(a**2)
print(a and b)
print( a or c)

