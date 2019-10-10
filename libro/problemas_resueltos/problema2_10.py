A = int ( input ( "Escribe un numero entero positivo para A: "))
B = int ( input ( "Escribe otro numero entero positivo para B: "))
C = int ( input ( "Escribe otro numero entero positivo para C: "))
if A > B:
    if A > C:
        print(f"El valor de A es el mayor y es {A}.")
    elif A == C:
        print(f"Los valores de A y C son iguales a {A} y son los mayores.")
    else:
        print(f"El valor de C es el mayor y es de {C}.")
elif A == B:
        if A > C:
            print(f"Los valores de A y B son iguales a {A} y son los mayores.")
        elif A == C:
            print(f"Los valores de A, B y C son iguales y tienen valor de {A}.")
        else:
            print(f"El valor de C es el mayor y es de {C}.")
elif B > C:
    print(f"El valor de B es el mayor y es de {B}.")
elif B == C:
    print(f"Los valores de B y C son iguales a {B} y son los mayores.")
else:
    print(f"El valor de C es el mayor y es {C}.")
print("Fin del programa.")



