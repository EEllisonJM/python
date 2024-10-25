import matplotlib.pyplot as plt

# Datos de ventas simuladas
ventas = [
    {"id_producto": 1, "nombre": "Papas", "cantidad": 5, "total": 50.0},
    {"id_producto": 2, "nombre": "Soda", "cantidad": 3, "total": 45.0},
    {"id_producto": 3, "nombre": "Hamburguesa", "cantidad": 7, "total": 56.0}
]

# Extraer los nombres de productos y los totales de ventas
nombres_productos = [venta["nombre"] for venta in ventas]
totales_ventas = [venta["total"] for venta in ventas]

# Crear la gráfica de barras
plt.figure(figsize=(8, 6))
plt.bar(nombres_productos, totales_ventas, color='blue')
plt.title('Ventas por Producto')
plt.xlabel('Producto')
plt.ylabel('Total de Ventas')

# Mostrar la gráfica
plt.show()