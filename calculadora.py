print("Calculadora\n")
print("Seleccione la operación\n")
print("Suma: 1")
print("Resta: 2")
print("Multplicación: 3")
print("División: 4")
print("División Entera: 5")
print("Exponente: 6")
print("Resto: 7")
numero_uno = float(input("ponga el primer valor: \n"))
numero_dos = float(input("ponga el segundo valor: \n"))
operacion_tipo = float (input("Ponga el numero de la operación: \n"))

if operacion_tipo == 1:
    print("El resultado de la suma es", numero_uno + numero_dos,) 
if operacion_tipo == 2:
    print(numero_uno - numero_dos)
if operacion_tipo == 3:
    print(numero_uno * numero_dos)
if operacion_tipo == 4:
    print("El resultado de la division es", numero_uno / numero_dos,) 
if operacion_tipo == 5:
    print("El resultado de la división entera es", numero_uno // numero_dos,) 

else:
    print("La opción no esta disponible")


