#Titulo
print("Calcular edad Actual")
#ENTRADA
user_day = input("Ingrese su dia de nacimiento: ")
user_month = input("Ingrese su mes de nacimiento(En numeros): ")
user_year = input("Ingrese su año de nacimiento: ")
#PROCESAMIENTO
user_day = int(user_day)
user_month = int(user_month)
user_year = int(user_year)

#Declarar los dias dependiendo del mes
day1 = 0
if(user_month == 1):
    day1 = 31
elif(user_month == 2):
    day1 = 28
elif(user_month == 3):
    day1 = 31
elif(user_month == 4):
    day1 = 30
elif(user_month == 5):
    day1 = 31
elif(user_month == 6):
    day1 = 30
elif(user_month == 7):
    day1 = 31
elif(user_month == 8):
    day1 = 31
elif(user_month == 9):
    day1 = 30
elif(user_month == 10):
    day1 = 31
elif(user_month == 11):
    day1 = 30
elif(user_month == 12):
    day1 = 31
else:
    day1 = 31
#Condicional por si el usuario ingresa año 2022 y Mes de Junio
if(user_year == 2022 and user_month == 6):
    day1 = 1

#Errores
incorrect_day = False
incorrect_month = False
incorrect_year = False

if(user_day < 1 or user_day > day1):
    incorrect_day = True
if(user_month < 1 or user_month > 12):
    incorrect_month = True
if(user_year < 1900 or user_year > 2022):
    incorrect_year = True
if(user_year == 2022 and user_month > 6):
    incorrect_month = True

#Calcular edad del usuario
edad_actual = 2022 - user_year

if(user_month >= 6):
    edad_actual -= 1
    if (user_month == 6 and user_day == 1):
        edad_actual += 1


#SALIDA
if(incorrect_day == True):
    print("Numero de dia incorrecto")
if(incorrect_month == True):
    print("Numero de mes incorrecto")
if(incorrect_year == True):
    print("Numero de año incorrecto")
if(incorrect_day == False and incorrect_month == False and incorrect_year == False):
    print("Su edad actual es: ", edad_actual, "años de edad")