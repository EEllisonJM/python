import tkinter as tk
from tkinter import ttk
import sqlite3
import os

# Esto es peligroso, solo ejecutar si se quiere eliminar la base de datos
def eliminar_db():
    archivo = "BASE_DE_DATOS.db"
    try:
        if os.path.exists(archivo):
            os.remove(archivo)
            print(f"Archivo '{archivo}' eliminado exitosamente.")
        else:
            print(f"El archivo '{archivo}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error al intentar eliminar el archivo: {e}")

# Conectar o crear la base de datos
def conectar_db():
    conn = sqlite3.connect("BASE_DE_DATOS.db")
    cursor = conn.cursor()
    
    # Crear la tabla usuarios si no existe
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL,
        pais TEXT NOT NULL
    )
    """)
    
    conn.commit()
    conn.close()

# Función para agregar o actualizar los datos
def agregar_o_actualizar():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    pais = combo_pais.get()  # Usar el valor seleccionado del Combobox
    
    if nombre and edad and pais:
        conn = sqlite3.connect("BASE_DE_DATOS.db")
        cursor = conn.cursor()

        # Verificar si hay una fila seleccionada
        if tree.selection():
            # Actualizar la fila seleccionada
            item_id = tree.selection()[0]
            valores = tree.item(item_id, 'values')
            cursor.execute("UPDATE usuarios SET nombre = ?, edad = ?, pais = ? WHERE id = ?",
                           (nombre, edad, pais, valores[0]))
            conn.commit()

            # Actualizar la vista en el Treeview
            tree.item(item_id, values=(valores[0], nombre, edad, pais))
        else:
            # Insertar nuevos datos
            cursor.execute("INSERT INTO usuarios (nombre, edad, pais) VALUES (?, ?, ?)", (nombre, edad, pais))
            conn.commit()

            # Insertar los datos directamente en el Treeview
            tree.insert("", "end", values=(cursor.lastrowid, nombre, edad, pais))

        conn.close()
        limpiar_campos()

    else:
        print("Por favor completa todos los campos.")

# Función para cargar los datos de la base de datos y mostrarlos en la tabla
def cargar_datos():
    conn = sqlite3.connect("BASE_DE_DATOS.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, edad, pais FROM usuarios")
    filas = cursor.fetchall()
    for fila in filas:
        tree.insert("", "end", values=fila)
    conn.close()

# Función para eliminar los datos seleccionados
def eliminar_datos():
    if tree.selection():
        item_id = tree.selection()[0]
        valores = tree.item(item_id, 'values')
        conn = sqlite3.connect("BASE_DE_DATOS.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (valores[0],))
        conn.commit()
        conn.close()

        # Eliminar la fila del Treeview
        tree.delete(item_id)
        limpiar_campos()

# Función para seleccionar una fila y mostrar los datos en los campos de entrada
def seleccionar_fila(event):
    for item in tree.selection():
        item_id = tree.item(item, "values")
        entry_nombre.delete(0, tk.END)
        entry_nombre.insert(tk.END, item_id[1])
        entry_edad.delete(0, tk.END)
        entry_edad.insert(tk.END, item_id[2])
        combo_pais.set(item_id[3])  # Setear el valor del Combobox de acuerdo a la fila seleccionada

# Limpiar los campos de entrada y deseleccionar cualquier fila
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    # combo_pais.set("")
    # Deseleccionar cualquier fila en el Treeview
    for item in tree.selection():
        tree.selection_remove(item)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Tabla con formulario estilo CRUD")

ventana.geometry("600x400")

# Crear la base de datos y la tabla si no existen
conectar_db()

# Crear el formulario para agregar datos
form_frame = tk.Frame(ventana)
form_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

# Etiquetas y campos de texto en el formulario
tk.Label(form_frame, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(form_frame)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Edad").grid(row=1, column=0, padx=5, pady=5)
entry_edad = tk.Entry(form_frame)
entry_edad.grid(row=1, column=1, padx=5, pady=5)

# Combobox para seleccionar país
tk.Label(form_frame, text="País").grid(row=2, column=0, padx=5, pady=5)
combo_pais = ttk.Combobox(form_frame, values=["México", "Estados Unidos", "Canadá", "España"], state="readonly")
combo_pais.grid(row=2, column=1, padx=5, pady=5)
combo_pais.set("México")  # Valor por defecto

# Botones para las operaciones CRUD
boton_agregar_actualizar = tk.Button(form_frame, text="Agregar/Actualizar", command=agregar_o_actualizar)
boton_agregar_actualizar.grid(row=3, column=0)

boton_eliminar = tk.Button(form_frame, text="Eliminar", command=eliminar_datos)
boton_eliminar.grid(row=3, column=1)

# Botón para limpiar los campos y deseleccionar
boton_limpiar = tk.Button(form_frame, text="Limpiar", command=limpiar_campos)
boton_limpiar.grid(row=3, column=2)

# Crear un frame para la tabla
tabla_frame = tk.Frame(ventana)
tabla_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Crear la tabla con Treeview
columns = ("ID", "Nombre", "Edad", "País")
tree = ttk.Treeview(tabla_frame, columns=columns, show="headings")
tree.heading("ID", text="ID")
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

# Evento para seleccionar una fila
tree.bind("<ButtonRelease-1>", seleccionar_fila)

# Cargar los datos al iniciar la aplicación
cargar_datos()

# Ejecutar la ventana
ventana.mainloop()
