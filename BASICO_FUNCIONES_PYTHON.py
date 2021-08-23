#!/usr/bin/env python
# coding: utf-8

# In[1]:


def saludar ():
    print("Hola, esto se llama desde adentro de la función saludar()")
saludar()


# In[4]:


def tabla_del_5():
    for i in range (10):
        print(f"5 * {i} = {5*i}")
        
tabla_del_5()


# In[5]:


def prueba():
    n=10
    return n
prueba()


# In[6]:


n


# In[7]:


n=10

def prueba():
    print(n)

prueba()


# In[8]:


def test():
    print(n)
prueba()


# In[9]:


def test():
    o = 5
    print(o)
test()

o = 10

test ()
print(o)


# In[ ]:


#Retorno de valores


# In[10]:


def funcion():
    return "Este texto es el retorno de funcion()"
funcion()


# In[13]:


def funcion():
    return [1,2,3,4,5]
print(funcion())


# In[15]:


print(funcion()[3:])


# In[16]:


def funcion():
    return "Mensaje número 1",1994,[1,2,3]
funcion()


# In[ ]:


text, año, liston = funcion ()


# In[29]:


text


# In[30]:


año


# In[31]:


liston


# In[ ]:


#Argumentos y PARAMETROS


# In[33]:


def  resta(a,b):
    return a - b


# In[34]:


resta(1,2)


# In[36]:


def resta(a=None,b=None):
    if a == None or b == None:
        print("Error: enviar dos números a la función")
        return
    else:
        return a-b
resta(2,1)


# In[ ]:





# In[ ]:


#ARGUMENTOS POR VALOR


# In[37]:


def duplicar(numero):
    return numero*2
n = 10
duplicar(n), n


# In[ ]:


#Argumentos por REFERENCIA


# In[47]:


def duplicar_seq(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
    return numeros

notas_a = list(range(5))

notas_b = duplicar_seq(notas_a)


# In[48]:


notas_a, notas_b


# In[53]:


notas_c = list(range(6))
notas_d = duplicar_seq(notas_c[:])
notas_c, notas_d


# In[ ]:


#ARGUMENTOS INDETERMINADOS







# In[54]:


def argumentar(*args):
    print(args)
    
argumentar(5,"Johel Yun",[0,1,2,3,4])


# In[55]:


def argumentar(*args):
    for elemento in args:
        print(args)
    

argumentar(5,"johel yun",[0,1,2,3,4])


# In[ ]:


def nombrar(**kwargs):
    print(kwars)
    
nombrar(id=5,nombre="Felix Feliciano",notas=[10,10,20,3,4])


# In[56]:


def nombrar(**kwargs):
    for kwarg in kwargs:
        print(kwarg)
        
nombrar(id=5,nombre="Felix Feliciano",notas=[10,10,20,3,4])


# In[57]:


def nombrar(**kwargs):
    for clave in kwargs:
        print(clave," ", kwargs[clave])
        
           
nombrar(id=5,nombre="Felix Feliciano",notas=[10,10,20,3,4])


# In[59]:


def super_nominacion(*args, **kwargs):
    suma = 0
    for e in args:
        suma += e
    print("El promedio indeterminado es {}".format(suma/len(args)))
    for clave in kwargs:
        print(clave, "\t", kwargs[clave])

super_nominacion(10,10,20,3,4, id=5,nombre="Victor liliput", edad=27, notas= [10,10,20,3,4])


# In[ ]:


# Funciones RECURSIVAS


# In[60]:


def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print(num, "boom")
    print("Fin de función", num)

cuenta_atras(5)
    


# In[61]:


def factorial(num):
    print("Valor inicial --->", num)
    if num > 1:
        num = num * factorial(num-1)
    print("Valor final--->", num)
    return num

factorial(5)


# In[ ]:


#Funciones INTEGRADAS


# In[ ]:


n = int("8")
n


# In[63]:


f = float("10.5")
f, type(f)


# In[64]:


bin(19)


# In[65]:


hex(1)


# In[66]:


hex(10)


# In[70]:


int("0b10011",2)


# In[67]:


abs(-10)


# In[68]:


round(5.5)


# In[69]:


pow(2,3)


# In[ ]:


#OTRAS FUNCIONES importantes  









# In[ ]:


"PARA SEPARAR UNA CADENA".split()


# In[ ]:


"esto pone todo en mayusculas".upper()


# In[ ]:


"esto poner todo en minusculas".lower()


# In[ ]:


"esto todo lo capitaliza".title()


# In[74]:


a,b,c,d = zip(["A","B","C","D"],[10,12,13,14])


# In[75]:


a,b,c,d


# In[ ]:


# LAMBA



# In[76]:


def doblar (num):
    resultado = num * 2
    return resultado

doblar(10)


# In[79]:


def doblar (num):
    return num *2

doblar(20)


# In[82]:


def doblar(num): return num * 2

doblar(5)


# In[83]:


lambda num: num * 2


# In[ ]:


doblar = lambda num: num * 2


# In[84]:


doblar = lambda num : num * 2

doblar (5)


# In[85]:


impar = lambda num :num %2 != 0
impar(5)


# In[86]:


revertir = lambda cadena: cadena[::-1]

revertir("camarada")


# In[88]:


sumar = lambda x,y : x + y
sumar(1,2)

