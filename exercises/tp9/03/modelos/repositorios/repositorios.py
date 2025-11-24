from modelos.repositorios.repositorio_libro import RepositorioLibro
from modelos.repositorios.repositorio_prestamos import RepositorioPrestamos
from modelos.repositorios.repositorio_socios import RepositorioSocios


repo_libros = None
repo_socios = None
repo_prestamos = None

def obtener_repositorio_libros():
    global repo_libros
    if repo_libros is None:
        repo_libros = RepositorioLibro()
    return repo_libros


def obtener_repositorio_socios():
    global repo_socios
    if repo_socios is None:
        repo_socios = RepositorioSocios()
    return repo_socios

def obtener_repositorio_prestamos():
    global repo_prestamos
    if repo_prestamos is None:
        repo_prestamos = RepositorioPrestamos()
    return repo_prestamos