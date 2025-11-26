from flask import Blueprint, request, jsonify
from modelos.repositorios.repositorios import obtener_repositorio_examen_asignado, obtener_repositorio_alumno, obtener_repositorio_tema
from modelos.entidades.examenasignado import ExamenAsignado


bp_examen_asignado = Blueprint("rutas_examenes_asignados", __name__)
repo = obtener_repositorio_examen_asignado()
repo_alumnos = obtener_repositorio_alumno()
repo_temas = obtener_repositorio_tema()

@bp_examen_asignado.route("/examenes", methods=["GET"])
def todos():
    examenes = repo.obtenerTodos()
    todos_examenes = []
    for e in examenes:
        todos_examenes.append(e.toDiccionario())

    return jsonify(todos_examenes), 200


@bp_examen_asignado.route("/examenes/<int:legajo>", methods=["GET"])
def examenxlegajo(legajo):
    examen = repo.obtenerPorLegajo(legajo)
    if examen:
        return jsonify(examen.toDiccionario()), 200
    else:
        return jsonify({"mensaje": f"No se encontro el examen asignado al alumno con el legajo {legajo}"}), 404
    

@bp_examen_asignado.route("/examen", methods = ["POST"])
def agregarExamen():
    if request.is_json:
        datos_nuevos = request.get_json()
        alumno = repo_alumnos.obtenerPorLegajo(datos_nuevos["legajo"])
        if alumno:
            lista_temas = repo_temas.obtenerTodos()
            import random
            tema_selecionado = random.choice(lista_temas)
            examen = ExamenAsignado(alumno.obtenerLegajo(), tema_selecionado.obtenerNumero(), True)
            if repo.agregarExamenAsignado(examen):
                return jsonify({"mensaje": "Examen asignado correctamente", "examen_asignado": examen.toDiccionario()}), 201
            else:
                return jsonify({"mensaje": "No se pudo agregar el examen asignado"}), 400
        else:
            return jsonify({"mensaje": "Alumno no encontrado"}), 404
    else:
        return jsonify({"mensaje": "La solicitud debe ser en formato JSON"}), 400