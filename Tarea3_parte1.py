#Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego,
# solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.

nombres = input("Por favor ingrese un numero ")
#casual = int(casual)
nombres_list = input(" Por favor ingrese el siguiente numero de palabras separadas por una coma " + str(nombres), )
ejemplo = nombres_list.split(",")
#case1 = list(map(int, input().split()))
print("La lista tiene un total de ", len(ejemplo), "palabras")
print("La lista creada es ", ejemplo)

