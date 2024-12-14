Gestión de Inventario
Este es un programa de gestión de inventario que permite realizar operaciones básicas sobre productos almacenados en una base de datos SQLite. Utiliza la biblioteca colorama para mejorar la experiencia de usuario con colores en la terminal.

Funcionalidades Implementadas
Agregar producto: Permite agregar nuevos productos al inventario. Se requiere ingresar el nombre, descripción, categoría, cantidad y precio del producto.
Mostrar productos: Muestra todos los productos actualmente almacenados en el inventario.
Actualizar cantidad de producto: Permite actualizar la cantidad de un producto específico a través de su ID.
Eliminar producto: Permite eliminar un producto del inventario mediante su nombre.
Buscar producto: Permite buscar productos por su ID, nombre o categoría.
Reporte bajo stock: Muestra los productos cuyo stock esté por debajo de un valor definido por el usuario.

Base de Datos
La aplicación utiliza una base de datos SQLite llamada inventario.db y tiene una tabla llamada productos que almacena la siguiente información:
id: Identificador único del producto (autoincremental).
nombre: Nombre del producto.
cantidad: Cantidad disponible del producto.
descripcion: Descripción del producto.
precio: Precio del producto.
categoria: Categoría del producto.

Uso Interactivo
El programa se ejecuta en un menú interactivo en la terminal. Cada opción está numerada y permite realizar las diferentes operaciones mencionadas anteriormente.
Al seleccionar una opción, el sistema solicita la información necesaria y realiza la operación correspondiente.