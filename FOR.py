#!/usr/bin/env python
# coding: utf-8

# In[ ]:


numeros = [1,2,3,5,6,7,8,9,10]
inidice = 0

while (indice < len(numeros)):
    print(numeros[indice])
    inidice +=1


# In[2]:


for i in numeros:
    print(i)


# In[1]:


indice = 0
numeros = [0,1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    numeros[indice] *= 10
numeros


# In[8]:


numeros = [0,1,2,3,4,5,6,7,8,9,10]
for indice,numero in enumerate (numeros):
    numeros[indice] *= 10
numeros


# In[9]:


cad = "Hola, mi gente"
for caracter in cad:
    print(caracter)


# In[13]:


cad = "Hola mi gente"
for caracter in cad:
    cad+="*"
print(cad)


# In[14]:


cad_2 =""
for caracter in cad:
    cad_2 += "*"
print(cad,"\n", cad_2)


# In[15]:


cad_3 = ""
for caracter in cad:
    cad_3 += caracter*3
cad_3


# In[16]:


range(0, 10, 2)


# In[17]:


print(range(10),type(range(10)))


# In[18]:


for i in range(10):
    print(i)


# In[19]:


for i in range(5,30,3):
    print(i)


# In[21]:


lista = list(range(10))

for i in lista:
    print(lista)
    print(i)


# In[23]:


for i in range(5):
    print(range(5))
    print(i)
    


# In[ ]:




