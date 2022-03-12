numeros = []

for i in range(0, 5, 1):
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)

busqueda = int(input("Digite el numero a buscar: "))

loTengo = False
for numero in numeros:
    if(busqueda == numero):
        loTengo = True
        break
    else:
        loTengo = False

if(loTengo != False):
    print("Se lo tengo papa")
else:
    print("No lo tengo")