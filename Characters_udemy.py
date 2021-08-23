#!/usr/bin/env python
# coding: utf-8

# In[1]:


equipo = []

personajes = {'Nombre':'Sova',
             'Clase':'tira flecha',
              'Nación':'Rusia'
             }
equipo.append(personajes);
print(equipo)


personajes = {'Nombre':'Vernon',
             'Clase':'Stoner',
              'Nación':'Jamaica'
             }
equipo.append(personajes);



personajes = {'Nombre':'Gonzer',
             'Clase':'Malimbo',
              'Nación':'Las vegas'
             }
equipo.append(personajes);
equipo



for e in equipo:
    print(e["Nombre"],",",e["Clase"],"oriundo de ", e["Nación"]);


# In[ ]:




