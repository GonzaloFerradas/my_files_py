#Conjunción

print("Conjunción (and)")
num_uno = int(input("Escribe un número mayor a 2 y menor a 5:"))
if num_uno > 2 and num_uno < 5:
    print("El número", num_uno,"cumple con la condicón. \n")
else:
    print("el número", num_uno, "NO cumple con la condición. \n")

#Disyunción
print("Disyunción  (or)")
palabra = input ("Para cumplir con la condición escribir la palabra si o yes:")
if palabra == "si" or palabra == "yes":
    print("La condicón se ha cumplido")
else:
    print("La condición NO se ha cumplido")

#Negación
print("Negación(not)") 
num_uno = int(input("Introduce un número igual a 5"))
if not num_uno == 5:
    print("\n El número es diferente de cinco y SI cumple con la condición")
else:
    print("\n El número es igual a cinco y NO cumple con la condición ")

