from modelos.repositorios.repositorio_socios import RepositorioSocios

repo_socios = None


def obtener_repositorio_socios():
    global repo_socios
    if repo_socios is None:
        repo_socios = RepositorioSocios()
    return repo_socios