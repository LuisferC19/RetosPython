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