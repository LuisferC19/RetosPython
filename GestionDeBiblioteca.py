# Reto 3 - Gestion de Biblioteca
# Taller de Python Intermedio
 
# aqui guardo todos los libros de la biblioteca
libros = []
 
# aqui guardo los usuarios y los libros que tienen prestados
usuarios = {}
 
 
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