# Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.
lista_remplazar=['Alberto', 'Carmen', 'Benito', 'Carmen']
print('Dígame cuántas palabras tiene la lista?\n', 'La lista tiene ' + str(len(lista_remplazar)), 'palabras')

print('Dígame la palabra 1\n ' 'La palabra 1 es ' + str(lista_remplazar[0]))
print('Dígame la palabra 2\n ' 'La palabra 2 es ' + str(lista_remplazar[1]))
print('Dígame la palabra 3\n ' 'La palabra 3 es ' + str(lista_remplazar[2]))
print('Dígame la palabra 4\n ' 'La palabra 4 es ' + str(lista_remplazar[3]))

print("Seleccione un nombre de la  lista creada")
actual=input()
print('El nombre que sera remplazado es ', actual)
lista_remplazar.remove(actual)
print('Digite el nombre que desea agregar a la lista')
replazo=input()
lista_remplazar.append(replazo)
print('La lista ha sido modificada ', str(lista_remplazar))
