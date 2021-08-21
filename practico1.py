print("****************************************")   
print("*Sistema de control vacacional pizeria Bernal*")
print("****************************************")
nombre_empleado = input("Ponga el nombre del colaborador: \n")
clave_departamento = int (input("Ponga la clave del departamento:\n"))
antiguedad_empleado = float(input("Ponga antiguedad del colaborador"))

if clave_departamento == 1:
    if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
        print("el colaborador", nombre_empleado, "tiene derecho a 6 días de vacaciones")
    elif antiguedad_empleado >=2 and antiguedad_empleado <=6:
        print("el colaborador", nombre_empleado, "tiene derecho a 14 días de vacaciones")
    elif antiguedad_empleado >= 7:
        print ("el colaborador", nombre_empleado, "tiene derecho a 20 días de vacaciones")
    else:
        print( nombre_empleado, "no tiene derecho a vacacionar")

elif clave_departamento == 2:
    if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
        print("el colaborador", nombre_empleado, "tiene derecho a 7 días de vacaciones")
    elif antiguedad_empleado >=2 and antiguedad_empleado <=6:
        print("el colaborador", nombre_empleado, "tiene derecho a 15 días de vacaciones")
    elif antiguedad_empleado >= 7:
        print ("el colaborador", nombre_empleado, "tiene derecho a 22 días de vacaciones")
    else:
        print( nombre_empleado, "no tiene derecho a vacacionar")

elif clave_departamento == 3:
    if antiguedad_empleado >= 1 and antiguedad_empleado < 2:
        print("el colaborador", nombre_empleado, "tiene derecho a 10 días de vacaciones")
    elif antiguedad_empleado >=2 and antiguedad_empleado <=6:
        print("el colaborador", nombre_empleado, "tiene derecho a 20 días de vacaciones")
    elif antiguedad_empleado >= 7:
        print ("el colaborador", nombre_empleado, "tiene derecho a 30 días de vacaciones")
    else:
        print( nombre_empleado, "no tiene derecho a vacacionar")

else:
    print("no existe esa clave, vuelva a intentarlo")