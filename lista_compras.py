#!/usr/bin/env python
# coding: utf-8

# In[13]:


lista_de_compras= ["Huevos","Leche","Queso","Jabón"]
lista_con_precios= ["Huevos",1.5,"Leche",2,"Queso",3.5,"Jabón",5]


# In[14]:


lista_de_compras


# In[15]:


print(f"""Los {lista_con_precios[0]} cuestan {lista_con_precios[1]} )
La {lista_con_precios[2]} cuesta {lista_con_precios[3]}""")


# In[22]:


lista_con_precios[1] = 0.9

print(f'''{lista_con_precios}
Los {lista_con_precios[0]} cuestan {lista_con_precios[1]}''')


# In[24]:


range(0,20,2)


# In[28]:


numeros= range(0,20,2);

lista_numeros= list(numeros);

print(f"""{numeros}
{lista_numeros}""")


# In[29]:


lista_numeros.append(4)
print(lista_numeros)


# In[ ]:


lista_numeros +[23, 66, 12, 35,'hola''overtime','cygne']


# In[37]:


nu_lista = lista_numeros[:5]+[23,66,12,35,'hola','overtime','cygne']
nu_lista


# In[32]:


len([1,2,3])


# In[33]:


len(nu_lista)


# In[34]:


3 in[1,2,3]


# In[38]:


'hola' in nu_lista


# In[39]:


nu_lista[:4] = ["Platos",14,"Libros","Teclados"]
nu_lista


# In[40]:


fila_1=[1,2,3]
fila_2=[4,5,6]
fila_3=[7,8,9]
matriz=[fila_1,fila_2,fila_3]
matriz


# In[41]:


matriz[0]== fila_1


# In[42]:


matriz[0][1]


# In[43]:


matriz[1][1:]


# In[ ]:




