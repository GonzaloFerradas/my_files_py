#!/usr/bin/env python
# coding: utf-8

# In[2]:


x=30

nombre='la cartuja de parma' ''


# In[3]:


x


# In[4]:


nombre


# In[6]:


x.__add__(10)


# In[20]:


diccionario = {'uno':x, 'dos':x.__add__(10)} ;

diccionario 


# In[22]:


print(f"{nombre.title()} cuesta {diccionario['uno']} pesos\n y el otro libro {diccionario['dos']} pesos.")


# In[ ]:


dir(x)


# In[ ]:


help(x)

