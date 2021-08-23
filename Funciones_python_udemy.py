#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Función area rectangulo

def area_rectangulo(base, altura):
    return base * altura

print(area_rectangulo(15,10))


# In[ ]:


#fucion ares circulo


# In[9]:


import math

def area_circulo(radio):
    return (radio**(float(input("ponga el radio del circulo: \n"))))* math.pi
print(area_circulo(5))


# In[13]:


def relacion (a,b):
    if a > b:
        return   1
    elif a < b:
        return-1
    else:
        return   0
print(relacion(5,10))
print(relacion(10,5))
print(relacion(5,5))


# In[14]:


def intermedio(a,b):
    return (a+b)/2

intermedio(-12,24)


# In[16]:


def recortar(num, minimo, maximo):
    if num < minimo:
        return minimo
    elif num > maximo:
        return maximo
    return num
print(recortar(15,0,10))
    


# In[ ]:





# In[38]:


numeros = [1,2,3,4]
numeros

def separar(lista):
    lista.sort()
    pares = []
    impares = []
    for n in lista:
        if n%2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares

pares, impares = separar(numeros)
print(pares)
print(impares)


# In[ ]:





# In[ ]:




