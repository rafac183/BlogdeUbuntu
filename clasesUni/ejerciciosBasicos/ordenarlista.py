lista=[15,10,11,100,1000,12,13,5,111,99,901,8721,10278,19,17]
lista2 = []
for nro in lista:
    if(len(lista2) == 0):
        lista2.append(nro)
    else:
        elemInsert = False
        i = 0
        while(i < len(lista2)):
            if(nro < lista2[i]):
                lista2.insert(i, nro)
                elemInsert = True
                i = len(lista2)
            i += 1
        if(elemInsert == False):
            lista2.append(nro)
print(lista2)