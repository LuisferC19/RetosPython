# Reto 2: Inventario de productos
class Inventario:
    # Creamos el constructor de la clase que se ejecuta al crear el objeto
    def __init__(self):
        # La lista que se usara sera inventario que guardara cada producto con su : [nombre, cantidad]
        self.inventario = []

    #Funcion para agregar productos
    def agregar_producto(self):
        nombre = input("Ingrese el nombre del producto: ") #Con input perimte ingresar datos desde terminal
        cantidad = int(input("Ingrese la cantidad del producto: ")) #Se ingresa la cantida y la convierte a entero

        if cantidad <= 0: #Se verifica que la cantidad del producto sea mayor a cero
            print("La cantidad debe ser mayor a 0")
            return

        # Usamos filter para buscar en el inventario el producto cuyo nombre coincida
        ListaResultado = list(filter(lambda producto: producto[0] == nombre, self.inventario))

        # Si la lista "rListaResultado" no está vacía, significa que el producto ya existe
        if len(ListaResultado) > 0:
            producto_existente = ListaResultado[0]  
            producto_existente[1] = producto_existente[1] + cantidad  
        else:
            self.inventario.append([nombre, cantidad])# Si no existe el producto, lo agregamos como nuevo
        
        print("_ _ _ _ _ __ _ _ __ _ _ _ __ _ _ _ ")
        print(" Producto agregado correctamente  \n")

    # Funcion para mostrar el inventario
    def mostrar_inventario(self):
        if len(self.inventario) == 0:#Validamos si el inventario esta vacio
            print("El inventario está vacío\n")
            return

        print("\n  El Inventario Actual Es :")

        #  Usamos "map" para transforma cada producto  de la lista [nombre, cantidad] en un texto
        ListaMostrar = list(map(lambda producto: "El producto es :"+ producto[0] + "\nLa cantidad que hay es : " + str(producto[1])+ "\n-------------------------", self.inventario))

        #Recorremos la lista (ListaMostrar) con los datos ingresados y imprimimos la nueva lista del inventario
        for linea in ListaMostrar:
            print(linea)

    #Fucion para vender producto
    def vender_producto(self):
        nombre = input("Ingrese el nombre del producto a vender: ")#ingresamos el nombre del producto a vender

        # Usamos filter para busca el producto por nombre que sea el mismo que en la funcion "agregar_producto"
        ListaResultado = list(filter(lambda producto: producto[0] == nombre, self.inventario))

        # Si no se encontró ningún producto con ese nombre
        if len(ListaResultado) == 0:
            print("El producto no existe en el inventario\n")
            return

        producto = ListaResultado[0]   # Tomamos el producto encontrado

        cantidad_vender = int(input("Ingrese la cantidad a vender: "))#Ingresamos la cantidad que venderemos del producto

        if cantidad_vender <= 0:#Validamos la cantidad ingresada
            print("La cantidad tiene que ser mayor a 0\n")
            return

        if cantidad_vender > producto[1]:
            print("No hay suficientes productos en el stock.\n Solo quedan " + str(producto[1]) + " unidades\n")
            return

        producto[1] = producto[1] - cantidad_vender # Se resta la cantida vendida del producto que esta en inventario

        if producto[1] == 0:# En caso que se venda toda la cantidad del produto se elimina de la Lista "producto"
            self.inventario.remove(producto)
            print("Venta realizada. El producto se agotó y fue eliminado del inventario.\n")
        else:
            print("Venta realizada. Quedan " + str(producto[1]) + " unidades.\n")

    # Funcion para mostrar el menu principal
    def mostrar_menu(self):
        print("_ _ _ _ _Gestion De Inventario_ _ _ _ _")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Vender producto")
        print("4. Salir")


if __name__ == "__main__":
    sistema = Inventario()   # Creamos el objeto de la clase inventario
    opcion = 0

    while opcion != 4:
        sistema.mostrar_menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            sistema.agregar_producto()
        elif opcion == 2:
            sistema.mostrar_inventario()
        elif opcion == 3:
            sistema.vender_producto()
        elif opcion == 4:
            print("Saliendo del sistema")
        else:
            print("Opción inválida, intente de nuevo.\n")