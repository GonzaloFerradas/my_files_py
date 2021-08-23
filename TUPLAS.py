#EJERCICIO DE TUPLAS, LAS TUPLAS SON INMUTABLES
#PARA MODIFICAR UNA TUPLA HAY QUE PASARLA A LISTA

tupla = ('Lunes', 'Martes', 'Miércoles')
tupla_multi = ([1,2,3],'a',71.4,tupla)

tupla_multi

tupla_multi[-1]

lista =list(tupla)
lista

lista[0] = 'Domingo'
lista

tupla_multi.count(71.4)

