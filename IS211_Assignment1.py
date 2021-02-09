#!/usr/bin/env python
# coding: utf-8

# In[43]:


def listDivide(l,divide=2): 
    c=0
    for e in l:
        ife%divide == 0
    c=c+1
    return c
       


# In[41]:


def testListDivide (self):
    if listDivide9([1,2,3,4,5])!=2:
        return "Test case failed"
    elif listDivide([2,4,6,8,10])!=5:
        return "Test case failed"
    elif listDivide([30,54,63,98,100],divide=10)!=2:
        return "Test case failed"
    elif listDivide([])!=0:
        return "Test case failed"
    elif listDivide([1,2,3,4,5],divide=1)!=5:
        return "Test case failed"


# In[ ]:




