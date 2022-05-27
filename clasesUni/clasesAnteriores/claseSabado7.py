#CONSTANTES

#ENTRADA
texto = input("Ingrese una Palabra: ")
a = False
e = False
i = False
o = False
u = False
#PROCESAMIENTO
texto = texto.lower()

if("a" in texto):
    a = True
if("e" in texto):
    e = True
if("i" in texto):
    i = True
if("o" in texto):
    o = True
if("u" in texto):
    u = True
#SALIDA
if(a == True):
    print("'a' Esta presente en el texto")
elif(a != True):
    print("'a' No esta presente en el texto")
if(e == True):
    print("'e' Esta presente en el texto")
elif(e != True):
    print("'e' No esta presente en el texto")
if(i == True):
    print("'i' Esta presente en el texto")
elif(i != True):
    print("'i' No esta presente en el texto")
if(o == True):
    print("'o' Esta presente en el texto")
elif(o != True):
    print("'o' No esta presente en el texto")
if(u == True):
    print("'u' Esta presente en el texto")
elif(u != True):
    print("'u' No esta presente en el texto")
