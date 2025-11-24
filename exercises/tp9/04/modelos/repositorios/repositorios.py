from modelos.repositorios.repositorio_polizas import RepositorioPolizas


repo_polizas = None

def obtener_repositorio_polizas():
    global repo_polizas
    if repo_polizas is None:
        repo_polizas = RepositorioPolizas()

    return repo_polizas