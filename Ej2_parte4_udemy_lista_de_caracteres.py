#!/usr/bin/env python
# coding: utf-8

# In[7]:


lista = ["avila", "cafe", "este", "narración","buda","extra","salida"]

lista2 = []
suma = 0 
for item in lista:
    if(len(item) >= 2 and (item[0] == item[-1])):
        suma +=1
        lista2.append(item)
suma, lista2


# In[ ]:


#Numeros impares


# In[ ]:


while (True):
    numero = int(input("Introduce un número impar:"))
    if (numero % 2 !=0):
        break 


# In[ ]:


###Sumar los numeros enteros oares desde el 0 hasta el 100


# In[ ]:


num=0
suma=0

while num <= 100:
    if (num % 2 == 0):
        suma += num
    num += 1
print(suma)


# In[ ]:




