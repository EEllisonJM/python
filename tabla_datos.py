import tkinter as tk
from tkinter import ttk

# Lista para almacenar los datos de la tabla (en caso de que quieras persistirlos)
datos = [
    ("Nombre", "Edad", "País"),  # Encabezados de la tabla
]

def agregar_datos():
    # Obtener los valores de los campos de texto
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    pais = entry_pais.get()
    
    # Verificar que los campos no estén vacíos
    if nombre and edad and pais:
        # Insertar los datos directamente en el Treeview
        tree.insert("", "end", values=(nombre, edad, pais))
        
        # Agregar los datos a la lista (opcional si quieres persistirlo en memoria)
        datos.append((nombre, edad, pais))

        # Limpiar las entradas de texto después de agregar los datos
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        entry_pais.delete(0, tk.END)
    else:
        print("Por favor completa todos los campos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Tabla con formulario estilo BorderLayout")

# Configurar el tamaño de la ventana y layout
ventana.geometry("600x400")

# Crear el formulario para agregar datos (ubicado en la parte superior)
form_frame = tk.Frame(ventana)
form_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

# Etiquetas y campos de texto en el formulario
tk.Label(form_frame, text="Nombre").grid(row=0, column=0, padx=5, pady=5) # Fila 0, Columna 0
entry_nombre = tk.Entry(form_frame)
entry_nombre.grid(row=0, column=1, padx=5, pady=5) # Fila 0, Columna 1

tk.Label(form_frame, text="Edad").grid(row=1, column=0, padx=5, pady=5) # Fila 1, Columna 0
entry_edad = tk.Entry(form_frame)
entry_edad.grid(row=1, column=1, padx=5, pady=5) # Fila 1, columna 1

tk.Label(form_frame, text="País").grid(row=2, column=0, padx=5, pady=5) # Fila 2, Columna 0
entry_pais = tk.Entry(form_frame)
entry_pais.grid(row=2, column=1, padx=5, pady=5) # Fila 2, Columna 1

# Botón para agregar datos
boton_agregar = tk.Button(form_frame, text="Agregar", command=agregar_datos)
boton_agregar.grid(row=3, column=1, padx=5, pady=10) # Fila 3, Columna 1

# Crear un frame para la tabla
tabla_frame = tk.Frame(ventana)
tabla_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Crear la tabla con Treeview para simular la tabla
columns = ("Nombre", "Edad", "País")
tree = ttk.Treeview(tabla_frame, columns=columns, show="headings")
tree.heading("Nombre", text="Nombre")
tree.heading("Edad", text="Edad")
tree.heading("País", text="País")

for col in columns:
    tree.column(col, anchor="center", width=150)

# Posicionar la tabla en la ventana
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Agregar scrollbar
scrollbar = ttk.Scrollbar(tabla_frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Ejecutar la ventana
ventana.mainloop()
