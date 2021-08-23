lista_de_compras= ["Huevos","Leche","Queso","Jabón"]
lista_con_precios= ["Huevos",1.5,"Leche",2,"Queso",3.5,"Jabón",5]

print(lista_de_compras)

type(lista_de_compras)

print(f"""Los {lista_con_precios[0]} cuestan {lista_con_precios[1]} )
La {lista_con_precios[2]} cuesta {lista_con_precios[3]}""")

#MUTABILIDAD hay que distinguir entre objetos MUTABLES, como las listas y objetvos INMUTABLES


lista_con_precios[1] = 0.9

print(f'''{lista_con_precios}
Los {lista_con_precios[0]} cuestan {lista_con_precios[1]}''')

#RANGE

range(0,20,2)

numeros= range(0,20,2);

lista_numeros= list(numeros);

print(f"""{numeros}
{lista_numeros}""")

#COMO USAR EL APPEND

lista_numeros.append(4)
print(lista_numeros)

lista_numeros +[23, 66, 12, 35,'hola','overtime','cygne']

nu_lista = lista_numeros[:5]+[23,66,12,35,'hola','overtime','cygne']
nu_lista


print('hola' in nu_lista)

#----------------------------------------------------------------------------------------------
#-------------------------COMO ACTUALIZAR LISTAS------------------------------------------------
# ----------------------------------------------------------------------------------------------

nu_lista[:4] = ["Platos",14,"Libros","Teclados"]
nu_lista
print (nu_lista)

#LISTAS ANIDADAS------------------------------------------------
# ----------------------------------------------------------------------------------------------
fila_1=[1,2,3]
fila_2=[4,5,6]
fila_3=[7,8,9]
matriz=[fila_1,fila_2,fila_3]
matriz

print(matriz)

#COMO ACCEDER A LAS LISTAS! NOS MOVEMOS POR LA MATRIZ COMO NEO

matriz[0]== fila_1
matriz[0][1]
matriz[1][1:]