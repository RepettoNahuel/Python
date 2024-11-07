# Clase Producto para definir cada producto con nombre y cantidad
class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def mostrar_info(self):
        """Muestra la información del producto en formato de texto"""
        print(f"Producto: {self.nombre} - Cantidad: {self.cantidad}")

# Lista para almacenar el inventario de productos
inventario = []

def mostrar_menu():
    print("\n=== Menú de Gestión de Productos ===")
    print("1. Agregar producto al inventario")
    print("2. Mostrar productos registrados")
    print("3. Salir")

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intente nuevamente.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número entero para la cantidad.")
    producto = Producto(nombre, cantidad)  
    inventario.append(producto)  
    print(f"Producto '{nombre}' agregado con éxito.")

def mostrar_inventario():
    if not inventario:
        print("No hay productos en el inventario.")
    else:
        print("\n=== Inventario de Productos ===")
        for producto in inventario:
            producto.mostrar_info()

# Bucle principal del menú interactivo
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")