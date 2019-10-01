S = int ( input ( "Introduzca el sueldo del trabajador: "))
if S < 1000:
    NS = S * 1.15
    print(f"El sueldo del trabajador es de {NS}.")
else:
    NS = S * 1.12
    print(f"El sueldo del trabajador es de {NS}.")

