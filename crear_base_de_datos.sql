CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono INTEGER NOT NULL,
    direccion TEXT NOT NULL,
    fecha_creado DATE DEFAULT current_timestamp
);

CREATE TABLE IF NOT EXISTS producto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio INTEGER NOT NULL,
    existencia INTEGER NOT NULL,
	caducidad DATE,
    fecha_creado DATE DEFAULT current_timestamp
);

CREATE TABLE IF NOT EXISTS proveedor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono INTEGER NOT NULL,
    direccion TEXT NOT NULL,
    fecha_creado DATE DEFAULT current_timestamp
);

CREATE TABLE IF NOT EXISTS venta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER,
    total INTEGER NOT NULL,
    fecha DATE DEFAULT current_timestamp,
    FOREIGN KEY (id_cliente) REFERENCES clientes (id)
);

CREATE TABLE IF NOT EXISTS detalle_de_venta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_venta INTEGER,
    id_producto INTEGER,
    precio INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    subtotal INTEGER NOT NULL,
    FOREIGN KEY (id_venta) REFERENCES venta (id),
    FOREIGN KEY (id_producto) REFERENCES producto (id)
);
