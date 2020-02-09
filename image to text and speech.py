#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pytesseract 


# In[2]:


from PIL import Image


# In[3]:


import pyttsx3


# In[4]:


from googletrans import Translator


# In[5]:


img = Image.open('WhatsApp Image 2020-02-08 at 5.52.50 PM.png')
print(img)


# In[14]:


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'


# In[15]:


result = pytesseract.image_to_string(img)


# In[ ]:


with open('abc.txt',mode ='w') as file:      
      
                 file.write(result) 
                 print(result) 


# In[9]:


p = Translator()


# In[10]:


k = p.translate(result,dest='english')


# In[11]:


print(k)


# In[12]:


engine = pyttsx3.init()


# In[ ]:


engine.say(k)
engine.runAndWait()


# In[ ]:




