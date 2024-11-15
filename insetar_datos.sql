-- Insertar clientes
INSERT INTO clientes (nombre, telefono, direccion) VALUES
('Juan Pérez', 1234567890, 'Calle Principal 123'),
('María López', 9876543210, 'Avenida Secundaria 456');

-- Insertar proveedores
INSERT INTO proveedor (nombre, telefono, direccion) VALUES
('Proveedor A', 1111111111, 'Calle Comercio 1'),
('Proveedor B', 2222222222, 'Calle Comercio 2'),
('Proveedor C', 3333333333, 'Calle Comercio 3');

-- Insertar productos
INSERT INTO producto (nombre, precio, existencia) VALUES
('Producto 1', 50, 100),
('Producto 2', 30, 200),
('Producto 3', 40, 150),
('Producto 4', 25, 300),
('Producto 5', 60, 80),
('Producto 6', 100, 50),
('Producto 7', 70, 120),
('Producto 8', 20, 400),
('Producto 9', 150, 30),
('Producto 10', 200, 25);

-- Insertar ventas
INSERT INTO venta (id_cliente, total, fecha) VALUES
(1, 150, '2024-11-15'),
(2, 200, '2024-11-15'),
(1, 300, '2024-11-15');

-- Insertar detalles de ventas
INSERT INTO detalle_de_venta (id_venta, id_producto, precio, cantidad, subtotal) VALUES
-- Venta 1
(1, 1, 50, 2, 100),
(1, 2, 30, 1, 30),
(1, 3, 40, 1, 40),
-- Venta 2
(2, 4, 25, 5, 125),
(2, 5, 60, 1, 60),
(2, 6, 100, 1, 100),
-- Venta 3
(3, 7, 70, 2, 140),
(3, 8, 20, 3, 60),
(3, 9, 150, 1, 150);
