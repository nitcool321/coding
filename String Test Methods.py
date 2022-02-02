#!/usr/bin/env python
# coding: utf-8

# In[3]:


StringName = "Python1"


# In[4]:


StringName.isalpha() # A-Z and a-z only,, not even space


# In[5]:


StringName.isalnum() #alphabets & numbers


# In[6]:


StringName.islower() #All small, similarly isupper()


# In[7]:


StringName.isdecimal() #Digits only


# In[8]:


StringName.isspace()


# In[9]:


word = "Hello Python. To be honest, you are the best"


# In[20]:


# if StringName.isspace():
#     break #break only works with for and while loop
# else:
#     not(StringName.isalnum())
#     print("String has special character") #Ctrl+/ - Select all, To comment/de-comment


# In[21]:


name = input("Enter Name: ") #Positional Formatting


# In[23]:


sal = float(input("Enter Salary: "))


# In[25]:


age = int(input("Enter age: "))


# In[26]:


print("Name - ",name, "Salary - ",sal, "Age - ",age) #Method 1 to display output. However lengthy


# In[31]:


print("Name - {}, Age - {}, Salary - {}" .format(name,age, sal)) 

# If more curly braces and passing less information, then error
# If 4 information and 3 curly braces then last one won't be taken
# Numbers/Index can be written inside curly braces starting from 0 which represents respective outputs
# \t - tab seperation, \n - New line


# In[32]:


#Print function has \n end by default and if , is used in print, space will be inserted


# In[8]:


print("Python is: ", end = "-")
print("Hello", "world", sep = ",,")


# In[ ]:


# if else elif, for loop practice done in assignments

