fecha = int(input("Coloque un año que se encuentre entre 1900 y 2199: "))
contador = int()
comienzo = int(1899)

while comienzo <= fecha:
    if (comienzo % 4 == 0 and (comienzo % 100 != 0 or comienzo % 400 == 0)): 
        contador = contador + 1
        comienzo = comienzo + 1
    
    else:
        comienzo = comienzo + 1
    
if 1900 < fecha < 2199:
    print ("El numero de años bisiestos entre 1900 y ", fecha,  "es: ", contador)
else:
    print ("El año que colocaste no se encuentra entre 1900 y 2199")