# Reto 3 - Gestion de Biblioteca
# Taller de Python Intermedio
 
# aqui guardo todos los libros de la biblioteca
libros = []
 
# aqui guardo los usuarios y los libros que tienen prestados
usuarios = {}


# funcion para agregar libros a la biblioteca
def agregar_libro(titulo, autor, genero, copias=1):
    # reviso si el libro ya esta registrado
    for l in libros:
        if l["titulo"].lower() == titulo.lower():
            print("Ese libro ya esta en la biblioteca")
            return
 
    # creo el diccionario del libro y lo agrego a la lista
    libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "copias": copias
    }
    libros.append(libro)
    print(f"Libro '{titulo}' agregado!")
 
 
# generador para buscar libros por algun campo
# uso yield para no cargar todo de golpe
def generador_busqueda(campo, valor):
    for l in libros:
        if valor.lower() in l[campo].lower():
            yield l
 
 
# busqueda con parametros opcionales
# asi puedo buscar por titulo, autor o genero segun lo que me pasen
def buscar_libro(titulo=None, autor=None, genero=None):
    resultados = []
 
    if titulo:
        resultados = list(generador_busqueda("titulo", titulo))
    elif autor:
        resultados = list(generador_busqueda("autor", autor))
    elif genero:
        resultados = list(generador_busqueda("genero", genero))
    else:
        print("Necesitas indicar por que quieres buscar")
        return
 
    if len(resultados) == 0:
        print("No encontre ningun libro con eso")
    else:
        print(f"\nEncontre {len(resultados)} libro(s):")
        for r in resultados:
            print(f"  Titulo: {r['titulo']}  |  Autor: {r['autor']}  |  Genero: {r['genero']}  |  Copias: {r['copias']}")
 
 
# funcion para prestar un libro
def prestar_libro(nombre_usuario, titulo):
    # si el usuario no existe lo creo
    if nombre_usuario not in usuarios:
        usuarios[nombre_usuario] = []
 
    for l in libros:
        if l["titulo"].lower() == titulo.lower():
            if l["copias"] > 0:
                l["copias"] -= 1
                usuarios[nombre_usuario].append(titulo)
                print(f"Se presto '{titulo}' a {nombre_usuario}")
            else:
                print(f"No hay copias disponibles de '{titulo}'")
            return
 
    print("Ese libro no existe en la biblioteca")
 
 
# funcion para devolver un libro
def devolver_libro(nombre_usuario, titulo):
    if nombre_usuario not in usuarios:
        print(f"{nombre_usuario} no esta registrado")
        return
 
    if titulo not in usuarios[nombre_usuario]:
        print(f"{nombre_usuario} no tiene prestado ese libro")
        return
 
    for l in libros:
        if l["titulo"].lower() == titulo.lower():
            l["copias"] += 1
            usuarios[nombre_usuario].remove(titulo)
            print(f"{nombre_usuario} devolvio '{titulo}', gracias!")
            return
 
 
# generador para obtener solo los libros que tienen copias
def libros_disponibles():
    for l in libros:
        if l["copias"] > 0:
            yield l
            # muestra todos los libros que tienen al menos una copia
def mostrar_disponibles():
    disponibles = list(libros_disponibles())
 
    if not disponibles:
        print("No hay libros disponibles ahorita")
        return
 
    print(f"\n{'Titulo':<28} {'Autor':<22} {'Genero':<14} Copias")
    print("-" * 72)
    for l in disponibles:
        print(f"{l['titulo']:<28} {l['autor']:<22} {l['genero']:<14} {l['copias']}")
 
 
# muestra los libros que tiene prestados un usuario
def ver_mis_libros(nombre_usuario):
    if nombre_usuario not in usuarios or not usuarios[nombre_usuario]:
        print(f"{nombre_usuario} no tiene libros prestados")
        return
 
    print(f"\nLibros que tiene {nombre_usuario}:")
    for t in usuarios[nombre_usuario]:
        print(f"  - {t}")
 
 
# menu de la consola
def menu():
    # cargo unos libros de ejemplo al inicio
    agregar_libro("Cien anos de soledad", "Gabriel Garcia Marquez", "Novela", 3)
    agregar_libro("El principito", "Antoine de Saint-Exupery", "Fantasia", 2)
    agregar_libro("1984", "George Orwell", "Distopia", 2)
    agregar_libro("Harry Potter", "J.K. Rowling", "Fantasia", 4)
    agregar_libro("Don Quijote", "Miguel de Cervantes", "Clasico", 1)
 
    while True:
        print("\n===== BIBLIOTECA =====")
        print("1. Agregar libro")
        print("2. Buscar libro")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Ver libros disponibles")
        print("6. Ver mis libros")
        print("0. Salir")
        print("======================")
 
        op = input("Opcion: ").strip()
 
        if op == "1":
            t = input("Titulo: ").strip()
            a = input("Autor: ").strip()
            g = input("Genero: ").strip()
            c = input("Copias (Enter para 1): ").strip()
            copias = int(c) if c.isdigit() else 1
            agregar_libro(t, a, g, copias)
 
        elif op == "2":
            print("Buscar por: 1-Titulo  2-Autor  3-Genero")
            modo = input("Opcion: ").strip()
            val = input("Que buscas?: ").strip()
            if modo == "1":
                buscar_libro(titulo=val)
            elif modo == "2":
                buscar_libro(autor=val)
            elif modo == "3":
                buscar_libro(genero=val)
            else:
                print("Opcion no valida")
 
        elif op == "3":
            u = input("Tu nombre: ").strip()
            t = input("Titulo del libro: ").strip()
            prestar_libro(u, t)
 
        elif op == "4":
            u = input("Tu nombre: ").strip()
            t = input("Titulo del libro: ").strip()
            devolver_libro(u, t)
 
        elif op == "5":
            mostrar_disponibles()
 
        elif op == "6":
            u = input("Tu nombre: ").strip()
            ver_mis_libros(u)
 
        elif op == "0":
            print("Adios!")
            break
 
        else:
            print("No entendi esa opcion")  # ← indentación corregida


if __name__ == "__main__":
    menu()