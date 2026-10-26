# Taller-5
Taller lógica de programación
Gestor de inventario con listas

Obejtivo

Programa de consola en Python para administrar el inventario de una tienda pequeña. Permite registrar, consultar, buscar, modificar y eliminar productos con su cantidad disponible. El objetivo es practicar el manejo de listas, índices, ciclos, condicionales y funciones.

Autor: Alejandro Rojas - Grupo: Alejandro Rojas, Sara Montaña

Requisitos

- Python 3.8 o superior.
- No requiere librerías externas, archivos ni bases de datos.
- Los datos se guardan solo en memoria: se pierden al cerrar el programa.

Instrucciones

1. Descarga o clona el repositorio.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta:

   ```
   python main.py
   ```

4. Elige una opción del menú escribiendo su número:

Opcion - Accion

1 Registrar un producto y su cantidad 
2 Mostrar todos los productos con su cantidad 
3 Buscar un producto por su nombre 
4 Modificar la cantidad de un producto 
5 Eliminar un producto 
6 Mostrar cuántos productos diferentes hay 
7 Mostrar el producto con mayor cantidad 
8 Salir 

Notas:
- La cantidad debe ser un número entero mayor o igual a 0.
- El nombre no distingue mayúsculas: "Arroz" y "arroz" son el mismo producto.
- Si se intenta registrar un producto que ya existe, el programa lo rechaza y sugiere usar la opción 4.

Como funciona

Se usan dos listas paralelas, `productos` y `cantidades`. El elemento en el índice `i` de cada lista corresponde al mismo producto (`productos[0]` y `cantidades[0]` describen el mismo producto). Cada operación modifica ambas listas con el mismo índice para mantenerlas sincronizadas.

Funciones que se usaron

- `buscar_indice(nombre)`: devuelve la posición del producto en la lista, o `-1` si no existe. La reutilizan casi todas las demás.
- `registrar_producto()`: valida nombre y cantidad, rechaza duplicados y agrega a ambas listas.
- `mostrar_inventario()`: recorre las listas con un ciclo y muestra cada producto numerado; avisa si está vacío.
- `buscar_producto()`: busca por nombre y muestra su cantidad, o indica que no existe.
- `modificar_cantidad()`: verifica que el producto exista y actualiza su cantidad.
- `eliminar_producto()`: verifica que exista y lo elimina de ambas listas con `pop(i)`.
- `mostrar_resumen()`: muestra cuántos productos diferentes hay.
- `producto_mayor_cantidad()`: muestra el producto con más unidades (en empate, el primero registrado).
- `mostrar_menu()`: ciclo principal del programa; maneja opciones inválidas con un mensaje.
