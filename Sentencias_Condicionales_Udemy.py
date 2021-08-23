#!/usr/bin/env python
# coding: utf-8

# In[2]:


if (True):
    print("Hey")


# In[ ]:


if (False):
    print("Hey")


# In[3]:


x=6

if x == 6:
    print("X vale 6")


# In[4]:


if x == 2:
    print("x vale 2")
if x == 6:
    print("x vale 6")


# In[14]:


a = 10
b = 5
if a == 10:
    print("A vale {}".format (a))
    if  b==5:
        print("B vale {}".format (b))


# In[19]:


if a==10 and b==5:
    print("A vale {}, y b vale {}".format(a,b))


# In[ ]:


z = 13
if z % 2 == 0:
    print(z, "Es un numero par")
else:
    print(z,"Es un número impar")


# In[ ]:


texto = input("¿Que desea hacer?\n ")
if texto == "SALUDAR":
    print("muy buenas noches")
elif texto == "RETIRARSE":
    print("Ok nos vemos")
else:
    print("vuelve a intentarlo")



# In[ ]:




