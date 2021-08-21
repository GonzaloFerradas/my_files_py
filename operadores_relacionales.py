print("Introduce dos números a comparar: \n")

num_uno = int (input("Introduce el primer número: "))
num_dos =int (input("Introduce"))

print("\n Los numeros a comparar son", num_uno, "y " , num_dos, "\n")

if num_uno == num_dos:
    print("Es igual...")
if num_uno != num_dos:
    print("El numero es diferente")
if num_uno < num_dos:
    print ("Es menor...")
if num_uno > num_dos:
    print("Es mayor...")
if num_uno >= num_dos :
    print ("Es mayor o igual ...")

