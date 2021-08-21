print ("Sistema para calcular el promedio de un alumno.")

nombre = input ("Para comenzar,  ¿Cual es tu nombre?: ")

matematicas = float(input(nombre + " ¿Cual es tu calificación en matematicas?: "))
quimica = float(input(nombre + " ¿Cual es tu calificación en quimica?: "))
biologia = float (input(nombre + " ¿Cual es tu calificación en biología?: "))

promedio = (matematicas + quimica + biologia) / 3
promedio = float (promedio)

if promedio >= 6: 
    print ('felicidades' + nombre + ' "aprobaste" con un promedio de : ', promedio ) 
    print ('felicidades' + nombre + ' "aprobaste" con un promedio de : ', round(promedio,2))
else: 
    print ("Lo sentimos" + nombre + "has 'reprobado' con un promedio de: " , promedio)
    print ("Lo sentimos" + nombre + "has 'reprobado' con un promedio de: " , round(promedio, 2))


print ("FIN.")
