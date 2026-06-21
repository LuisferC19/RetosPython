# Reto 2: Inventario de productos
class Inventario:
    def __init__(self):
        self.inventario = []

    def agregar_producto(self):
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))

        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0")
            return

        ListaResultado = list(filter(lambda producto: producto[0] == nombre, self.inventario))

        if len(ListaResultado) > 0:
            producto_existente = ListaResultado[0]
            producto_existente[1] = producto_existente[1] + cantidad
        else:
            self.inventario.append([nombre, cantidad])

        print("_ _ _ _ _ __ _ _ __ _ _ _ __ _ _ _ ")
        print(" Producto agregado correctamente  \n")

    def mostrar_inventario(self):  # ← indentación corregida
        if len(self.inventario) == 0:
            print("El inventario está vacío\n")
            return

        print("\n  El Inventario Actual Es :")

        ListaMostrar = list(map(lambda producto: "El producto es :" + producto[0] + "\nLa cantidad que hay es : " + str(producto[1]) + "\n-------------------------", self.inventario))

        for linea in ListaMostrar:
            print(linea)

    def mostrar_menu(self):
        print("_ _ _ _ _Gestion De Inventario_ _ _ _ _")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Vender producto")
        print("4. Salir")

    def vender_producto(self):
        nombre = input("Ingrese el nombre del producto a vender: ")

        ListaResultado = list(filter(lambda producto: producto[0] == nombre, self.inventario))

        if len(ListaResultado) == 0:
            print("El producto no existe en el inventario\n")
            return

        producto = ListaResultado[0]

        cantidad_vender = int(input("Ingrese la cantidad a vender: "))

        if cantidad_vender <= 0:
            print("La cantidad tiene que ser mayor a 0\n")
            return

        if cantidad_vender > producto[1]:
            print("No hay suficientes productos en el stock.\n Solo quedan " + str(producto[1]) + " unidades\n")
            return

        producto[1] = producto[1] - cantidad_vender

        if producto[1] == 0:
            self.inventario.remove(producto)
            print("Venta realizada. El producto se agotó y fue eliminado del inventario.\n")
        else:
            print("Venta realizada. Quedan " + str(producto[1]) + " unidades.\n")  # ← corregido


if __name__ == "__main__":
    inventario = Inventario()
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



