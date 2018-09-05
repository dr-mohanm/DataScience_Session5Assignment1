
# coding: utf-8

# In[2]:


# 1.Write a function to compute 5/0 and use try/except to catch the exceptions. 

# Function to compute 5/0
def divide_by_zero():
 return 5/0

# Try/except to catch the exceptions
try:
 divide_by_zero()
except ZeroDivisionError as err:
 print("Run-time 'divisible by 0' error: ", err)


# In[7]:


# 2.Implement a Python program to generate all sentences where subject is in ["Americans", "Indians"] 
# and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"]. 
# Hint: Subject,Verb and Object should be declared in the program as shown below. 
 
# subjects=["Americans ","Indians"]
# verbs=["play","watch"]
# objects=["Baseball","Cricket"]

# Output should come as below:
# Americans play Baseball.
# Americans play Cricket.
# Americans watch Baseball.
# Americans watch Cricket.
# Indians play Baseball.
# Indians play Cricket.
# Indians watch Baseball.
# Indians watch Cricket.

# Input lists
subjects = ["Americans", "Indians"]
verbs = ["play", "watch"]
objects = ["Baseball","cricket"]

# Use list comprehension instead of looping
sen_list = [(sub+" "+ vrb + " " + obj) for sub in subjects for vrb in verbs for obj in objects]
for sen in sen_list:
 print (sen+str('.'))

