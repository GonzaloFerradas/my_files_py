#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while (True):
    try:
        num = int(input("ingresa el num: "))
        "El número {} y al dividirlo da {}" .format(num,num/num)
        break
        
    except:
        print("volver a intentar!")   
    else:
        print("La ejecución fue excitosa")
        break


# In[ ]:


try:
    num = int(input("Ingresa un número: "))
    print ("9/ {} = {}".format(num,9/num))
except Exception as e:
    print("Ocurrio el siguiente error: ", type(e).__name__)


# In[ ]:




