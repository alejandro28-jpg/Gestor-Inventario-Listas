productos = []
cantidades = []

def buscar_indice(nombre):
    for i in range(len(productos)):
        if productos[i].lower() == nombre.lower():
            return i
    return -1

def registrar_producto():
    nombre = input('Nombre del producto: ').strip()

    if nombre == "":
        print('El nombre no puede estar vacio.')
        return

    if buscar_indice(nombre) != -1:
        print('Ese producto ya existe. Use la opcion 4 para cambiar su cantidad.')
        return 

    cantidad_texto = input('Cantidad disponible: ').strip()
    if not cantidad_texto.isdigit():
        print('La cantidad debe ser un numero entero no negativo.')
        return

    cantidad = int(cantidad_texto)
    
    productos.append(nombre)
    cantidades.append(cantidad)
    print('Producto registrado.')

def mostrar_inventario():
    if len(productos) == 0:
        print('El inventario esta vacio.')
        return

    print('---INVENTARIO---')
    for i in range(len(productos)):
        print(i + 1, '-', productos[i], '-', cantidades[i])

def buscar_producto():
    nombre = input('Nombre del producto a buscar: ').strip()
    i = buscar_indice(nombre)

    if i == -1:
        print('El producto no existe')
    else:
        print('Producto encontrado: ', productos[i], '-Cantidad', cantidades[i])

def modificar_cantidad():
    nombre = input('Nombre del producto a modificar: ').strip()
    i = buscar_indice(nombre)

    if i == -1:
        print('El producto no existe en el inventario.')
        return 

    print('Cantidad actual de', productos[i], ':', cantidades[i])
    cantidad_texto = input('Nueva cantidad: ').strip()

    if not cantidad_texto.isdigit():
        print('La cantidad debe ser un numero entero no negativo: ')
        return

    cantidades[i] = int(cantidad_texto)
    print('Cantidad actualizada.')


def eliminar_producto():
    nombre = input('Nombre del producto a eliminar: ').strip()
    i = buscar_indice(nombre)

    if i == -1:
        print('El producto no existe en el inventario.')
        return

    producto_eliminado = productos.pop(i)
    cantidades.pop(i)
    print('Producto eliminado: ', producto_eliminado)

def mostrar_resumen():
    print('Productos diferentes registrados: ', len(productos))

def producto_mayor_cantidad():
    if len(cantidades) == 0:
        print('El inventario esta vacio')
        return

    mayor = max(cantidades)
    i = cantidades.index(mayor)
    print('Producto con mayor cantidad: ', productos[i], 'Cantidad: ', mayor)

def mostrar_menu():

    while True:
        print("==================== MENU ======================")
        print('1. Registrar un producto y su cantidad disponible. ')
        print('2. Mostrar todos los productos con su cantidad. ')
        print('3. Buscar un producto por su nombre. ')
        print('4. Modificar la cantidad disponible de un producto. ')
        print('5. Eliminar un producto del inventario. ')
        print('6. Mostrar cuantos productos diferentes hay registrados. ')
        print('7. Mostrar el producto con la mayor cantidad disponible. ')
        print('8. Salir del programa. ')
        opcion = input("Elija una opcion: ").strip()

        if opcion == "1":
            registrar_producto()
        elif opcion == '2':
            mostrar_inventario()
        elif opcion == '3':
            buscar_producto()
        elif opcion == '4':
            modificar_cantidad()
        elif opcion == '5':
            eliminar_producto()
        elif opcion == '6':
            mostrar_resumen()
        elif opcion == '7':
            producto_mayor_cantidad()
        elif opcion == '8':
            print('Hasta luego')
            break
        else:
            print('Opcion no valida, intente de nuevo: ')




mostrar_menu()
