import mysql.connector
from utils.database import conexion

class ConProducto:
    def __init__(self, conexion):
        self.conexion = conexion

    def get_all(self):
        """Obtener todos los productos."""
        query = 'SELECT * FROM productos'
        return self.conexion.execute_read_query(query, ())

    def get_by_id(self, id_producto):
        """Obtener un producto por su ID."""
        query = 'SELECT * FROM productos WHERE id_producto = %s'
        return self.conexion.execute_read_query(query, (id_producto,))

    def insert(self, producto):
        """Insertar un nuevo producto."""
        query = 'INSERT INTO productos (nombre_producto, categoria, fecha_ingreso, fecha_vencimiento, cantidad, precio) VALUES (%s, %s, %s, %s, %s, %s)'
        return self.conexion.execute_query(query, (
            producto.nombre_producto,
            producto.categoria,
            producto.fecha_ingreso,
            producto.fecha_vencimiento,
            producto.cantidad,
            producto.precio
        ))

    def update(self, producto):
        """Actualizar un producto existente."""
        query = 'UPDATE productos SET nombre_producto = %s, categoria = %s, fecha_ingreso = %s, fecha_vencimiento = %s, cantidad = %s, precio = %s WHERE id_producto = %s'
        return self.conexion.execute_query(query, (
            producto.nombre_producto,
            producto.categoria,
            producto.fecha_ingreso,
            producto.fecha_vencimiento,
            producto.cantidad,
            producto.precio,
            producto.id_productos
        ))

    def delete(self, id_producto):
        """Eliminar un producto por su ID."""
        query = 'DELETE FROM productos WHERE id_producto = %s'
        return self.conexion.execute_query(query, (id_producto,))
class ConProveedor:
    def __init__(self, conexion):
        self.conexion = conexion

    def get_all(self):
        """Obtener todos los proveedores."""
        query = 'SELECT * FROM proveedores'
        return self.conexion.execute_read_query(query, ())

    def get_by_id(self, id_proveedor):
        """Obtener un proveedor por su ID."""
        query = 'SELECT * FROM proveedores WHERE id_proveedor = %s'
        return self.conexion.execute_read_query(query, (id_proveedor,))

    def insert(self, proveedor):
        """Insertar un nuevo proveedor."""
        query = 'INSERT INTO proveedores (nombre_proveedor, numero_proveedor, direccion_electronico) VALUES (%s, %s, %s)'
        return self.conexion.execute_query(query, (proveedor.nombre_proveedor, proveedor.numero_proveedor, proveedor.email))

    def update(self, proveedor):
        """Actualizar un proveedor existente."""
        query = 'UPDATE proveedores SET nombre_proveedor = %s, numero_proveedor = %s, direccion_electronico = %s WHERE id_proveedor = %s'
        return self.conexion.execute_query(query, (proveedor.nombre_proveedor, proveedor.numero_proveedor, proveedor.email, proveedor.id_proveedor))

    def delete(self, id_proveedor):
        """Eliminar un proveedor por su ID."""
        query = 'DELETE FROM proveedores WHERE id_proveedor = %s'
        return self.conexion.execute_query(query, (id_proveedor,))
class ConPedido:
    def __init__(self, conexion):
        self.conexion = conexion

    def get_all(self):
        """Obtener todos los pedidos."""
        query = 'SELECT * FROM pedidos'
        return self.conexion.execute_read_query(query, ())

    def get_by_id(self, id_pedido):
        """Obtener un pedido por su ID."""
        query = 'SELECT * FROM pedidos WHERE id_pedido = %s'
        return self.conexion.execute_read_query(query, (id_pedido,))

    def insert(self, pedido):
        """Insertar un nuevo pedido."""
        query = 'INSERT INTO pedidos (nombre_cliente, id_producto, id_proveedor, cantidad_pedido) VALUES (%s, %s, %s, %s)'
        return self.conexion.execute_query(query, (
            pedido.nombre_cliente,
            pedido.id_producto,
            pedido.id_proveedor,
            pedido.cantidad_pedido
        ))

    def update(self, pedido):
        """Actualizar un pedido existente."""
        query = 'UPDATE pedidos SET nombre_cliente = %s, id_producto = %s, id_proveedor = %s, cantidad_pedido = %s WHERE id_pedido = %s'
        return self.conexion.execute_query(query, (
            pedido.nombre_cliente,
            pedido.id_producto,
            pedido.id_proveedor,
            pedido.cantidad_pedido,
            pedido.id_pedido
        ))

    def delete(self, id_pedido):
        """Eliminar un pedido por su ID."""
        query = 'DELETE FROM pedidos WHERE id_pedido = %s'
        return self.conexion.execute_query(query, (id_pedido,))
