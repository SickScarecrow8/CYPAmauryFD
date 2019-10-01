M = input ( "Introduce tu matricula: ")
C1 = int ( input ( "Introduce la primera calificacion: "))
C2 = int ( input ( "Introduce la segunda calificacion: "))
C3 = int ( input ( "Introduce la tercer calificacion: "))
C4 = int ( input ( "Introduce la cuarta calificacion: "))
C5 = int ( input ( "Introduce la quinta calificacion: "))
P = (C1 + C2 + C3 + C4 + C5) / 5
if P >= 6:
    print(f"El alumno con matricula {M} y promedio de {P} esta aprobado.")
else:
    print(f"El alumno con matricula {M} y promedio de {P} esta reprobado.")

