import tkinter # Importar libreria
import math

def calcular_menor():
    a = float(entrada_a.get()) # Obtener valor desde la ventana (a) 
    b = float(entrada_b.get())# Obtener valor desde la ventana (b) 

    if a < b:
        txt_resultado.config(text=f"{a} Es menor")
    else:
        txt_resultado.config(text=f"{b} Es menor")

def calcular_mayor():
    a = float(entrada_a.get()) # Obtener valor desde la ventana (a) 
    b = float(entrada_b.get())# Obtener valor desde la ventana (b) 

    if a > b:
        txt_resultado.config(text=f"{a} Es mayor")
    else:
        txt_resultado.config(text=f"{b} Es mayor")

def calcular_hipotenusa():
    a = float(entrada_a.get()) # Obtener valor desde la ventana (a) 
    b = float(entrada_b.get())# Obtener valor desde la ventana (b) 
    fuerza = math.sqrt(a**2 + b**2)
    txt_resultado.config(text=f"Fuerza: {fuerza} N")

ventana = tkinter.Tk()
ventana.title("2 Numeros")
ventana.geometry("300x200")  # Dimensiones de la ventana (Base_x_Altura)

tkinter.Label(ventana, text="A : ").pack()

#Campos de texto
entrada_a = tkinter.Entry(ventana)
entrada_a.pack() # Coloca el widget debajo de txt_masa

tkinter.Label(ventana, text="B : ").pack()

entrada_b = tkinter.Entry(ventana)
entrada_b.pack() # Coloca el widget debajo de txt_aceleracion

tkinter.Button(ventana, text="Calcular Menor", command=calcular_menor).pack()
tkinter.Button(ventana, text="Calcular Mayor", command=calcular_mayor).pack()
tkinter.Button(ventana, text="Calcular Hipotenusa", command=calcular_hipotenusa).pack()

txt_resultado = tkinter.Label(ventana, text="")
txt_resultado.pack() # Coloca el widget debajo de entrada_a

ventana.mainloop()
