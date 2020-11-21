
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
L = len(alfabeto)


def codi_letra(letra):
    return alfabeto.index(letra)


def decodi_letra(n):
    return alfabeto[n]


def codifi_cadena(texto):
    return [codi_letra(c) for c in texto]


def decodifi_cadena(lista):
    return ''.join([decodi_letra(j) for j in lista])


def encripta(lista,N,e):
    return [pow(numero,e,N)for numero in lista]


def desencripta(lista,N,d):
    return [pow(numero,d,N)for numero in lista]


#def RSA()

print("Bienvenido al programa de Encriptacion en RSA")
print("Porfavor presione una de las siguientes opciones para continuar:""\n")
print("1.Encriptar""\n""2.Desencriptar""\n""3.Ver llaves publicas""\n""4.Salir""\n")

opcion = int(input("Su opcion: "))

p = 29
q = 31
N = p*q
e = 13
d = 517
clavepublic = (N,e)

while opcion != 4:
    if opcion == 1:
        print("Ahora va a encriptar")
        mensaje = str(input("Su mensaje a encriptar: "))
        mensaje = mensaje.upper()
        numeros = codifi_cadena(mensaje)
        cripto = encripta(numeros,N,e)
        print(cripto)
        print("Su mensaje a sido encriptado")
        print("Quiere corregir el mensaje \n 1.Si 2.Salir")
        opcion2 = int(input("Su opcion: "))
        if opcion2 == 1:
            mensaje = str(input("Su mensaje a encriptar: "))
            print("Su mensaje a sido encriptado")
            print("Quiere corregir el mensaje \n 1.Si 2.Salir")
            opcion2 = int(input("Su opcion: "))
        if opcion2 == 2:
            print("1.Encriptar""\n""2.Desencriptar""\n""3.Ver llaves publicas""\n""4.Salir""\n")
            opcion = int(input("Su opcion: "))
        else:
            print("Porfavor elija un opcion valida")
            print("Quiere corregir el mensaje \n 1.Si 2.Salir")
            opcion2 = int(input("Su opcion :"))
    if opcion == 2:
        desencriptado = desencripta(encripta,N,d)
        mensaje_densecriptado = decodifi_cadena(desencriptado)
        print(mensaje_densecriptado)
    if opcion == 3:
        print(clavepublic)
    if opcion == 4:
        print("Gracias por usar el programa de encriptacion")
        break
    else:
        print("Numero de opcion invalido""\n")
        print("Porfavor elija una opcion correcta")
        print("1.Encriptar""\n""2.Desencriptar""\n""3.Ver llaves publicas""\n""4.Salir""\n")

        opcion = int(input("Su opcion: "))
