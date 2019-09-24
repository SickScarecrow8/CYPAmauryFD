Edad = int( input("Dame tu edad: "))
INE = bool( int( input("Tienes INE (0 No / 1 Sí)?: ")))
if Edad >= 18 and INE == True:
    print("Es mayor de edad")
    print("Puede entrar al bar")
else:
    print("Eres menor de edad")
    print("Ve a tu casa a ver Pocoyó")
print("Fin del programa")

