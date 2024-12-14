from colorama import Fore, Style, init
import sqlite3

# Inicializar colorama para usar colores en la terminal
init()

# Conexión a la base de datos SQLite
conexion = sqlite3.connect('inventario.db')
cursor = conexion.cursor()

# Crear la tabla "productos" si no existe ya en la base de datos
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    descripcion TEXT,
    precio REAL,
    categoria TEXT
)
''')
conexion.commit()

# Mostrar el menú de opciones al usuario
def mostrar_menu():
    print(Fore.CYAN + "\n=== Menú de Gestión de Productos ===" + Style.RESET_ALL)
    print("1. Agregar producto.")
    print("2. Mostrar productos.")
    print("3. Actualizar cantidad de producto.")
    print("4. Eliminar producto.")
    print("5. Buscar producto.")
    print("6. Reporte bajo stock.")
    print("7. Salir")

# Función para agregar un nuevo producto al inventario
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    categoria = input("Ingrese la categoría del producto: ")

    # Validar que cantidad y precio sean valores positivos
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            if cantidad < 0 or precio < 0:
                print(Fore.RED + "La cantidad y el precio no pueden ser negativos. Intente nuevamente." + Style.RESET_ALL)
            else:
                break
        except ValueError:
            print(Fore.RED + "Por favor, ingrese valores numéricos para cantidad y precio." + Style.RESET_ALL)

    # Insertar los datos del producto en la base de datos
    cursor.execute("""
    INSERT INTO productos (nombre, cantidad, descripcion, precio, categoria)
    VALUES (?, ?, ?, ?, ?)
    """, (nombre, cantidad, descripcion, precio, categoria))
    conexion.commit()
    print(Fore.GREEN + f"Producto '{nombre}' agregado con éxito." + Style.RESET_ALL)

# Mostrar todos los productos del inventario
def mostrar_inventario():
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    if not productos:
        print(Fore.YELLOW + "No hay productos en el inventario." + Style.RESET_ALL)
    else:
        print("\n=== Inventario de Productos ===")
        # Iterar sobre cada producto para mostrar sus detalles
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[2]}, Precio: {producto[4]}, Categoría: {producto[5]}, Descripción: {producto[3]}")

# Actualizar la cantidad de un producto por ID o por nombre
def actualizar_cantidad():
    id_producto = input("Ingrese el ID del producto: ")
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    
    producto = cursor.fetchone()
    if producto:
        # Validar que la nueva cantidad sea positiva
        while True:
            try:
                nueva_cantidad = int(input(f"Ingrese la nueva cantidad para '{producto[1]}': "))
                if nueva_cantidad < 0:
                    print(Fore.RED + "La cantidad no puede ser negativa. Intente nuevamente." + Style.RESET_ALL)
                else:
                    break
            except ValueError:
                print(Fore.RED + "Por favor, ingrese un número entero válido." + Style.RESET_ALL)
        
        # Actualizar la cantidad del producto en la base de datos
        cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (nueva_cantidad, producto[0]))
        conexion.commit()
        print(Fore.GREEN + "Cantidad actualizada correctamente." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Producto no encontrado." + Style.RESET_ALL)

# Eliminar un producto del inventario
def eliminar_producto():
    nombre_producto = input("Ingrese el nombre del producto: ")
    cursor.execute("DELETE FROM productos WHERE nombre = ?", (nombre_producto,))
    
    conexion.commit()
    print(Fore.GREEN + "Producto eliminado correctamente si existía." + Style.RESET_ALL)

# Buscar un producto por ID, nombre o categoría
def buscar_producto():
    print("Buscar por: (1) ID, (2) Nombre, (3) Categoría")
    criterio = input("Seleccione una opción: ")
    if criterio == "1":
        id_producto = input("Ingrese el ID del producto: ")
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    elif criterio == "2":
        nombre_producto = input("Ingrese el nombre del producto: ")
        cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre_producto,))
    elif criterio == "3":
        categoria_producto = input("Ingrese la categoría del producto: ")
        cursor.execute("SELECT * FROM productos WHERE categoria = ?", (categoria_producto,))
    else:
        print(Fore.RED + "Opción inválida." + Style.RESET_ALL)
        return

    productos = cursor.fetchall()
    if productos:
        print(Fore.CYAN + "\n=== Resultados de la Búsqueda ===" + Style.RESET_ALL)
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[2]}, Precio: {producto[4]}, Categoría: {producto[5]}, Descripción: {producto[3]}")
    else:
        print(Fore.RED + "No se encontraron productos." + Style.RESET_ALL)

# Generar un reporte de productos con bajo stock
def reporte_bajo_stock():
    while True:
        try:
            limite_stock = int(input("Ingrese la cantidad límite para considerar bajo stock: "))
            break
        except ValueError:
            print(Fore.RED + "Por favor, ingrese un número entero." + Style.RESET_ALL)

    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite_stock,))
    productos = cursor.fetchall()
    if productos:
        print("\n=== Productos con bajo stock ===")
        # Mostrar los productos que cumplen con el criterio de bajo stock
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[2]}, Precio: {producto[4]}, Categoría: {producto[5]}, Descripción: {producto[3]}")
    else:
        print(Fore.GREEN + "No hay productos con bajo stock." + Style.RESET_ALL)

# Bucle principal para el menú interactivo
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        actualizar_cantidad()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        buscar_producto()
    elif opcion == "6":
        reporte_bajo_stock()
    elif opcion == "7":
        print("Saliendo del programa...")
        break
    else:
        print(Fore.RED + "Opción no válida. Intente nuevamente." + Style.RESET_ALL)

# Cerrar la conexión a la base de datos al salir del programa
conexion.close()