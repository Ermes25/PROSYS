from controllers.crud_controller import ConProveedor, ConPedido, ConProducto
from models.productos import productos_Modelos 
from models.pedidos import pedidos_Modelos  
from models.proveedores import proveedores_Modelos  
from utils.database import conexion 

def main():
    db = conexion('localhost', 'root', '', 'sistemainventario')

    producto_controller = ConProducto(db)
    pedido_controller = ConPedido(db)
    proveedor_controller = ConProveedor(db)

    while True:
        print("\n--- Menú de Gestión ---")
        print("1. Gestionar Productos")
        print("2. Gestionar Pedidos")
        print("3. Gestionar Proveedores")
        print("4. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            manage_products(producto_controller)
        elif choice == '2':
            manage_orders(pedido_controller)
        elif choice == '3':
            manage_providers(proveedor_controller)
        elif choice == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

    db.close()

def manage_products(controller):
    while True:
        print("\n--- Gestión de Productos ---")
        print("1. Listar Productos")
        print("2. Agregar Producto")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Volver al Menú Principal")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            productos = controller.get_all()
            for p in productos:
                print(p)
        elif choice == '2':
            nombre = input("Nombre del producto: ")
            categoria = input("Categoría: ")
            # `fecha_ingreso` se omite ya que es TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            fecha_vencimiento = input("Fecha de vencimiento (YYYY): ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            nuevo_producto = productos_Modelos(nombre, categoria, None, fecha_vencimiento, cantidad, precio)
            controller.insert(nuevo_producto)
            print("Producto agregado con éxito.")
        elif choice == '3':
            id_producto = int(input("ID del producto a actualizar: "))
            producto = controller.get_by_id(id_producto)
            if producto:
                producto.nombre_producto = input("Nuevo nombre del producto: ")
                producto.categoria = input("Nueva categoría: ")
                # `fecha_ingreso` se deja sin cambios
                producto.fecha_vencimiento = input("Nueva fecha de vencimiento (YYYY): ")
                producto.cantidad = int(input("Nueva cantidad: "))
                producto.precio = float(input("Nuevo precio: "))
                controller.update(producto)
                print("Producto actualizado con éxito.")
            else:
                print("Producto no encontrado.")
        elif choice == '4':
            id_producto = int(input("ID del producto a eliminar: "))
            controller.delete(id_producto)
            print("Producto eliminado con éxito.")
        elif choice == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def manage_orders(controller):
    while True:
        print("\n--- Gestión de Pedidos ---")
        print("1. Listar Pedidos")
        print("2. Agregar Pedido")
        print("3. Actualizar Pedido")
        print("4. Eliminar Pedido")
        print("5. Volver al Menú Principal")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            pedidos = controller.get_all()
            for p in pedidos:
                print(p)
        elif choice == '2':
            nombre_cliente = input("Nombre del cliente: ")
            id_producto = int(input("ID del producto: "))
            id_proveedor = int(input("ID del proveedor: "))
            cantidad_pedido = int(input("Cantidad del pedido: "))
            nuevo_pedido = pedidos_Modelos(nombre_cliente, id_producto, id_proveedor, cantidad_pedido)
            controller.insert(nuevo_pedido)
            print("Pedido agregado con éxito.")
        elif choice == '3':
            id_pedido = int(input("ID del pedido a actualizar: "))
            pedido = controller.get_by_id(id_pedido)
            if pedido:
                pedido.nombre_cliente = input("Nuevo nombre del cliente: ")
                pedido.id_producto = int(input("Nuevo ID del producto: "))
                pedido.id_proveedor = int(input("Nuevo ID del proveedor: "))
                pedido.cantidad_pedido = int(input("Nueva cantidad del pedido: "))
                controller.update(pedido)
                print("Pedido actualizado con éxito.")
            else:
                print("Pedido no encontrado.")
        elif choice == '4':
            id_pedido = int(input("ID del pedido a eliminar: "))
            controller.delete(id_pedido)
            print("Pedido eliminado con éxito.")
        elif choice == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def manage_providers(controller):
    while True:
        print("\n--- Gestión de Proveedores ---")
        print("1. Listar Proveedores")
        print("2. Agregar Proveedor")
        print("3. Actualizar Proveedor")
        print("4. Eliminar Proveedor")
        print("5. Volver al Menú Principal")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            proveedores = controller.get_all()
            for p in proveedores:
                print(p)
        elif choice == '2':
            nombre_proveedor = input("Nombre del proveedor: ")
            numero_proveedor = input("Número de teléfono del proveedor: ")
            direccion_electronico = input("Correo electrónico del proveedor: ")
            nuevo_proveedor = proveedores_Modelos(nombre_proveedor, numero_proveedor, direccion_electronico)
            controller.insert(nuevo_proveedor)
            print("Proveedor agregado con éxito.")
        elif choice == '3':
            id_proveedor = int(input("ID del proveedor a actualizar: "))
            proveedor = controller.get_by_id(id_proveedor)
            if proveedor:
                proveedor.nombre_proveedor = input("Nuevo nombre del proveedor: ")
                proveedor.numero_proveedor = input("Nuevo número de teléfono: ")
                proveedor.direccion_electronico = input("Nuevo correo electrónico: ")
                controller.update(proveedor)
                print("Proveedor actualizado con éxito.")
            else:
                print("Proveedor no encontrado.")
        elif choice == '4':
            id_proveedor = int(input("ID del proveedor a eliminar: "))
            controller.delete(id_proveedor)
            print("Proveedor eliminado con éxito.")
        elif choice == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
