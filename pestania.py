import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Pestañas en Tkinter")
root.geometry("400x300")

# Crear un widget Notebook (para las pestañas)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Crear el primer frame (pestaña)
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Pestaña 1")

# Contenido de la primera pestaña
label1 = tk.Label(tab1, text="Contenido de la Pestaña 1", font=("Arial", 14))
label1.pack(pady=20)

# Crear la segunda pestaña
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Pestaña 2")

# Contenido de la segunda pestaña
label2 = tk.Label(tab2, text="Contenido de la Pestaña 2", font=("Arial", 14))
label2.pack(pady=20)

# Crear la tercera pestaña
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Pestaña 3")

# Contenido de la tercera pestaña
label3 = tk.Label(tab3, text="Contenido de la Pestaña 3", font=("Arial", 14))
label3.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()
