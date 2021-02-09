#!/usr/bin/env python
# coding: utf-8

# In[21]:


class Book:
    author = ""
    title = ""
    
    def __init__(self, author, title):
        self.author = author
        self.title = title
        
    def display(self):
        print(self.title + "written by" +self.author)
        
obj1 = Book('John Steinback', 'Of Mice and Men')
obj2 = Book('Harper', 'To Kill a Mockongbird')

obj1.display()
print()
obj2.display()


# In[ ]:




