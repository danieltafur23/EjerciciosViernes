# #Creando tuplas en python

# estudiantes = ('Carlos', 'Juan Carlos')
# print(estudiantes)

# # estudiantes.append('martha')
# # print(estudiantes)

# #Recorriendo tuplas
# for estudiante in estudiantes:
#     print(estudiante)

# #Convertir tuplas en lista
# listaEstudiantes = list(estudiantes)
# print(listaEstudiantes)

#
tuplaNumeros=(50,45,20,30,40,87)

listaNumero=[]

for i in range(len(tuplaNumeros)):
    if(tuplaNumeros[i]>40):
        listaNumero.append(tuplaNumeros[i])

print(listaNumero)