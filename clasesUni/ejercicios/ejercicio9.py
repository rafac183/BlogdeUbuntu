#CONSTANTES
#Titulo
print("Determinar a que generacion pertenece")
#ENTRADAS
year = input("Ingrese Su Año de Nacimiento: ")
#PROCESAMIENTO
year = int(year)
silent = False
baby = False
x = False
y = False
z = False
a = False

if(year>=1928 and year<=1948):
    silent = True
elif(year>=1949 and year<=1968):
    baby = True
elif(year>=1969 and year<=1980):
    x = True
elif(year>=1981 and year<=1993):
    y = True
elif(year>=1994 and year<=2010):
    z = True
elif(year>=2011 and year<=2025):
    a = True
#SALIDA
if(silent==True):
    print("Eres Silent Generation")
elif(baby == True):
    print("Eres Baby Boomer")
elif(x == True):
    print("Eres X Generation")
elif(y == True):
    print("Eres Y Generation")
elif(z == True):
    print("Eres Z Generation")
elif(a == True):
    print("Eres A Generation")
