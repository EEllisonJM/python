# Entradas
n1 = input("Ingrese número 1 : ")
n2 = input("Ingrese número 2 : ")
n3 = input("Ingrese número 3 : ")

# Procesos
if n1 < n2:
    if n1 < n3:
        print(n1," ES MENOR") # Salida
    else:
        print(n3," ES MENOR") # Salida
else: # n2 es el menor
    if n2 < n3:
        print(n2," ES MENOR") # Salida
    else:
        print(n3," ES MENOR") # Salida