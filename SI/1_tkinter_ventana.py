# Ejemplo de interfaz gráfica con Tkinter
import tkinter as tk  # Es recomendable usar un alias más corto

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Información")
root.geometry("400x300")

# Agregar una etiqueta a la ventana
label = tk.Label(root, text="Bienvenido al Sistema de Ventas")
label.pack()

# Ejecutar el bucle principal de la interfaz
root.mainloop()
