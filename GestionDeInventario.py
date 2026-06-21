# Reto 2: Inventario de productos
class Inventario:
    # Constructor de la clase, inicializa los atributos del inventario
    def __init__(self):
        # La lista que guardara cada producto con su: [nombre, cantidad]
        self.inventario = []

    # Funcion para agregar productos al inventario
    def agregar_producto(self):
        nombre = input("Ingrese el nombre del producto: ") # Con input permite ingresar datos desde terminal
        cantidad = int(input("Ingrese la cantidad del producto: ")) # Se ingresa la cantidad y la convierte a entero

        if cantidad <= 0: # Se verifica que la cantidad del producto sea mayor a cero
            print("La cantidad debe ser mayor a 0")
            return

        # Usamos filter para buscar en el inventario el producto cuyo nombre coincida
        ListaResultado = list(filter(lambda producto: producto[0] == nombre, self.inventario))

        # Si la lista "ListaResultado" no esta vacia, significa que el producto ya existe
        if len(ListaResultado) > 0:
            producto_existente = ListaResultado[0]
            producto_existente[1] = producto_existente[1] + cantidad # Se suma la cantidad nueva a la existente
        else:
            self.inventario.append([nombre, cantidad]) # Si no existe el producto, lo agregamos como nuevo

        print("_ _ _ _ _ __ _ _ __ _ _ _ __ _ _ _ ")
        print(" Producto agregado correctamente  \n")

    # Funcion para mostrar el inventario
    def mostrar_inventario(self):
        if len(self.inventario) == 0: # Validamos si el inventario esta vacio
            print("El inventario está vacío\n")
            return

        print("\n  El Inventario Actual Es :")

        # Usamos "map" para transformar cada producto de la lista [nombre, cantidad] en un texto
        ListaMostrar = list(map(lambda producto: "El producto es :" + producto[0] + "\nLa cantidad que hay es : " + str(producto[1]) + "\n-------------------------", self.inventario))

        # Recorremos la lista con los datos ingresados e imprimimos el inventario
        for linea in ListaMostrar:
            print(linea)

    # Funcion para mostrar el menu principal
    def mostrar_menu(self):
        print("_ _ _ _ _Gestion De Inventario_ _ _ _ _")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Vender producto")
        print("4. Salir")

    # Funcion para vender producto
    def vender_producto(self):
        nombre = input("Ingrese el nombre del producto a vender: ") # Ingresamos el nombre del producto a vender

        # Usamos filter para buscar el producto por nombre
        ListaResultado = list(filter(lambda producto: producto[0] == nombre, self.inventario))

        # Si no se encontro ningun producto con ese nombre
        if len(ListaResultado) == 0:
            print("El producto no existe en el inventario\n")
            return

        producto = ListaResultado[0] # Tomamos el producto encontrado

        cantidad_vender = int(input("Ingrese la cantidad a vender: ")) # Ingresamos la cantidad a vender

        if cantidad_vender <= 0: # Validamos la cantidad ingresada
            print("La cantidad tiene que ser mayor a 0\n")
            return

        if cantidad_vender > producto[1]:
            print("No hay suficientes productos en el stock.\n Solo quedan " + str(producto[1]) + " unidades\n")
            return

        producto[1] = producto[1] - cantidad_vender # Se resta la cantidad vendida del inventario

        if producto[1] == 0: # Si se vende toda la cantidad, se elimina del inventario
            self.inventario.remove(producto)
            print("Venta realizada. El producto se agotó y fue eliminado del inventario.\n")
        else:
            print("Venta realizada. Quedan " + str(producto[1]) + " unidades.\n")


if __name__ == "__main__":
    inventario = Inventario() # Creamos el objeto de la clase
    opcion = 0

    while opcion != 4:
        inventario.mostrar_menu()
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            inventario.agregar_producto()
        elif opcion == 2:
            inventario.mostrar_inventario()
        elif opcion == 3:
            inventario.vender_producto()
        elif opcion == 4:
            print("Saliendo del programa")
        else:
            print("Opcion invalida, intente de nuevo.\n")



