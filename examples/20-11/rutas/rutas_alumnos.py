from flask import Blueprint, request, jsonify
from modelos.repositorios.repositorios import obtener_repositorio_alumno
from modelos.entidades.alumno import Alumno


bp_alumno = Blueprint("rutas_alumnos", __name__)
repo = obtener_repositorio_alumno()

@bp_alumno.route("/alumnos", methods=["GET"])
def todos():
    alumnos = repo.obtenerTodos()
    todos_alumnos = []
    for a in alumnos:
        todos_alumnos.append(a.toDiccionario())

    return jsonify(todos_alumnos), 200


@bp_alumno.route("/alumnos/<int:legajo>", methods=["GET"])
def alumnoxlegajo(legajo):
    alumno = repo.obtenerPorLegajo(legajo)
    if alumno:
        return jsonify(alumno.toDiccionario()), 200
    else:
        return jsonify({"mensaje": f"No se encontro el alumno con el legajo {legajo}"}), 404



@bp_alumno.route("/alumnos", methods = ["POST"])
def agregar():
    if request.is_json:
        datos_nuevos = request.get_json()
        try:
            nuevo_alumno = Alumno.fromDiccionario(datos_nuevos)

            if repo.agregarAlumno(nuevo_alumno):
                return jsonify({"mensaje":"se agrego correctamente el alumno", 
                                "nuevo_alumno":nuevo_alumno.toDiccionario()}), 201
            else:
                return jsonify({"mensaje":"no se pudo agregar el alumno"}), 400

        except Exception as e:
            return jsonify({"mensaje": str(e)}), 400
    else:
        return jsonify({"mensaje":"La solicitud debe ser en formato JSON"}), 400