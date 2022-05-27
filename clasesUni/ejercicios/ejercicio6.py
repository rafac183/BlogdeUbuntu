#Titulo
print("Codigo para determinar para sumar nros Divisibles entre 3")
#ENTRADAS
num1=input("Ingresa un numero: ")
num2=input("Ingresa un numero: ")

#PROCEDIMIENTO
num1=int(num1)
num2=int(num2)
uno_menor_que_dos = True
nro_no_divisible = False
res = 0
if(num1 >= num2):
    uno_menor_que_dos = False
else:
    i = num1
    while (i >= num1 and i <= num2):
        if (i % 3 == 0):
            res += i
        i += 1
#SALIDA
if(uno_menor_que_dos == False):
    print("Error El primero numero es Mayor o igual que el Segundo")
elif(nro_no_divisible == True):
    print("Ningun Numero es divisible por 3, por lo tanto el resultado es: ", res)
else:
    print("Resultado: ", res)