#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n_1 = float(input("Introdice un número: \n"))
n_2 = float(input("Introduce otro número: \n"))

print("¿Que quieres hacer?")
print("[1] Sumar los dos números")
print("[2] Restar los dos números")
print("[3] Multiplicar los dos números")

opcion = input("Ingresa una opción: \n")

if opcion == "1":
    print(f"La suma de {n_1} + {n_2} es {n_1+n_2}")
elif opcion == "2":
    print(f"La resta de {n_1} - {n_2} es {n_1-n_2}")
elif opcion == "3":
    print(f"La producto de {n_1} * {n_2} es {n_1*n_2}")
else:
    print("La opción ingresa es inválida")


# In[ ]:





# In[ ]:




