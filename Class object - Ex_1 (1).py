#!/usr/bin/env python
# coding: utf-8

# In[22]:


# creating line class with coor1, coor2 attribute and distance and slope as methods
import math
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    
    def distance(self):
        return math.sqrt( ((self.coor1[0]-self.coor2[0])**2)+((self.coor1[1]-self.coor2[1])**2) )
    
    def slope(self):
        return ((self.coor2[1] - self.coor1[1]))/((self.coor2[0] - self.coor1[0]))
    
       


# In[23]:


my_line=Line((3,2), (8,10))


# In[24]:


my_line.distance()


# In[26]:



my_line.slope()


# In[29]:


class Cylinder:
    
    #class object
    pi=3.14
    
    def __init__(self,height,radius):
        self.height=height
        self.radius=radius
        
    def volume(self):
        return Cylinder.pi * self.radius**2 *self.height
    
    def surface_area(self):
        return ((Cylinder.pi * self.radius**2 *self.height) + (2* Cylinder.pi * self.radius* self.height))
    
    


# In[33]:


my_cyl= Cylinder(2,3)


# In[34]:


my_cyl.surface_area()


# In[35]:


my_cyl.volume()

