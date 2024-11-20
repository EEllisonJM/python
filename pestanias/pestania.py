import tkinter as tk
from tkinter import ttk
from clientes import gestion_clientes

root = tk.Tk()
root.title("Aplicación con Pestañas")
root.geometry("800x600")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Primera pestaña
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Pestaña 1")
tk.Label(tab1, text="Contenido de la Pestaña 1").pack(pady=20)

# Segunda pestaña: Gestión de Clientes
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Gestión de Clientes")
gestion_clientes(tab2).pack(fill="both", expand=True)

root.mainloop()
