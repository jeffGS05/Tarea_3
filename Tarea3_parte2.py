#####Escriba un programa que permita crear una lista de palabras y que, a continuación, pida
# una palabra y diga cuántas veces aparece esa palabra en la lista.

objetivo2=['Carmen', 'Alberto', 'Benito', 'Carmen']
#Dígame cuántas palabras tiene la lista
print('La lista tiene ', len(objetivo2), 'palabras')

print('Dígame la palabra 1 ' 'La palabra 1 es ' + objetivo2[0])
print('Dígame la palabra 2 ' 'La palabra 2 es ' + objetivo2[1])
print('Dígame la palabra 3 ' 'La palabra 3 es ' + objetivo2[2])
print('Dígame la palabra 4 ' 'La palabra 4 es ' + objetivo2[3])


print('Dígame la palabra a buscar ')
clave=input()
print('La palabra ', clave, ' aparece ' + str(objetivo2.count(clave)), 'veces en la lista.')

print('Dígame cuántas palabras tiene la lista?\n La lista tiene ' + str(len(objetivo2)), 'palabras')

objetivo3=['Carmen', 'Alberto', 'Benito', 'Carmen']
print('Dígame la palabra 1 ' 'La palabra 1 es ' + objetivo3[0])
print('Dígame la palabra 2 ' 'La palabra 2 es ' + objetivo3[1])
print('Dígame la palabra 3 ' 'La palabra 3 es ' + objetivo3[2])
print('Dígame la palabra 4 ' 'La palabra 4 es ' + objetivo3[3])

print('La lista creada es\n' + str(objetivo3))

print('La palabra Alberto  aparece ' + str(objetivo3.count('Alberto')), 'veces en la lista.')

print('Dígame la palabra a buscar')
busqueda=input()

if busqueda in objetivo3:
    print('El nombre ', busqueda, 'si pertenece a la lista')
else:
    print('El nombre ', busqueda, 'no esta el la lista')
