from modelos.repositorios.repositorio_libro import RepositorioLibro


repo_libros = None

def obtener_repositorio_libros():
    global repo_libros
    if repo_libros is None:
        repo_libros = RepositorioLibro()
    return repo_libros