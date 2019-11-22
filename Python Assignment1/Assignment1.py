#!/usr/bin/env python
# coding: utf-8

# In[1]:


#SOLUTION QuestionNo:1
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


# In[5]:


#SOLUTION QuestionNo:2
import sys
print("'Python version and info'")
print (sys.version)
print (sys.version_info)


# In[7]:


#SOLUTION QuestionNo:3
import datetime
now = datetime.datetime.now()
print ("Current Date is: ")
print (now.strftime("%Y-%m-%d"))
print ("Current Time is:")
print (now.strftime("%H:%M:%S"))


# In[9]:


#SOLUTION QuestionNo:4
pi = 3.14
radius = float(input ("Enter the radius of the circle: "))
print ("The total area of the circle is" + str(radius) + " is: " + str(pi * radius**2))


# In[11]:


#SOLUTION QuestionNo:5
FirstName = input("Input your First Name: ")
LastName = input("Input your Last Name: ")
print ("It's reversed as:"  + LastName + " " + FirstName)


# In[21]:


#SOLUTION QuestionNo:6
numb1 = 23
numb2 = 28
sum = numb1 + numb2
print("Addition of 23 and 28 is: ")
print(sum)


# In[ ]:




