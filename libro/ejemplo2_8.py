CATE = int ( input ("Escribe tu categoria: "))
SUE = float ( input ("Ingresa tu sueldo: "))
NSUE = 0
if CATE == 1:
    NSUE = SUE * 1.15
elif CATE == 2:
    NSUE = SUE * 1.10
elif CATE == 3:
    NSUE = SUE * 1.08
elif CATE == 4:
    NSUE = SUE * 1.07
print(f"Estas en la categoria {CATE} y tu sueldo es {NSUE}.")
     
print("Fin del programa.")

