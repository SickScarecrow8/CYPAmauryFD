L1 = int ( input ("Inserte el primer lado del triangulo: "))
L2 = int ( input ("Inserte el segundo lado del triangulo: "))
L3 = int ( input ("Inserte el tercer lado del triangulo: "))
S = (L1 + L2 + L3)/2
A = (S * (S-L1) * (S-L2) * (S-L3)) ** 0.5
print(f"El area del triangulo es {A}")


