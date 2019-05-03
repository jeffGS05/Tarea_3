# Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista.

lista_eliminar=['Alberto', 'Carmen', 'Benito', 'Carmen']
print('La lista creada es la siguiete ', lista_eliminar)
print('De la lista mostrada anteriormente escoja un elemento para se eliminado')
eliminar=input()
while eliminar in lista_eliminar:
    lista_eliminar.remove(eliminar)
    print('El elememento ', eliminar, 'sera elinimado de la lista')
else:
    print('La lista no con tiene ese elemento')

print('El contenido de la lista actual es el siguente\n',lista_eliminar)