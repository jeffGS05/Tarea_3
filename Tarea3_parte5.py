#Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los nombres de la segunda lista.
lista1=['Carmen', 'Carmen', 'Alberto', 'Benito', 'David']
lista2=['Benito', 'Juan', 'Carmen']
print('Dígame cuántas palabras tiene la lista 1: ' + str(len(lista1)))
print('Dígame cuántas palabras tiene la lista 2: ' + str(len(lista2)))
print('La lista creada es: ', lista1)
print('La lista #2 creada es: ', lista2)
L1= set(lista1)
L2= set(lista2)
duplicados=L2.intersection(L1)

for duplicados in lista1:
   #print(duplicados)
   lista1.remove(duplicados)
print('La lista es ahora', lista1)

#print('Dígame cuántas palabras tiene la lista de palabras a eliminar ' + str(len(L1.intersection(L2))) + str(L1.intersection(L2)))

#La lista es ahora: ['Alberto', 'David']



