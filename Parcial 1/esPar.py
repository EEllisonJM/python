# Codigo para determinar si un número es par o es impar
# Entrada 
n = float(input("Ingrese un número : "))

# Procesos
aux = n/2
hasDecimals = aux - int(aux)>0 #Tiene decimales
if hasDecimals:
    print("ES IMPAR") # Salida
else:
    print("ES PAR") # Salida