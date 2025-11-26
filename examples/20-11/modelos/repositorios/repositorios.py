from modelos.repositorios.repositorio_alumno import RepositorioAlumno
from modelos.repositorios.repositorio_examenasignado import RepositorioExamenesAsignados
from modelos.repositorios.repositorio_tema import RepositorioTema

repo_alumno = None
repo_tema = None
repo_examen_asigando = None

def obtener_repositorio_alumno():
    global repo_alumno
    if repo_alumno is None:
        repo_alumno = RepositorioAlumno()
    return repo_alumno

def obtener_repositorio_tema():
    global repo_tema
    if repo_tema is None:
        repo_tema = RepositorioTema()
    return repo_tema

def obtener_repositorio_examen_asignado():
    global repo_examen_asigando
    if repo_examen_asigando is None:
        repo_examen_asigando = RepositorioExamenesAsignados()
    return repo_examen_asigando