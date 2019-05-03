#Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista igual a la primera,
# pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).

L1= ['Alberto', 'Carmen', 'Benito', 'Daniel']
print('Lista original\n ', L1)
L2= L1[::-1]
print('Lista creada en orden inverso\n ', L2)
