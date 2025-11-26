from modelos.entidades.tema import Tema
from modelos.repositorios.repositorios import obtener_repositorio_tema
from flask import Blueprint, jsonify, request



bp_tema = Blueprint("rutas_temas", __name__)

repo = obtener_repositorio_tema()

@bp_tema.route("/temas", methods = ["GET"])
def todos():
    temas = repo.obtenerTodos()
    todos_temas = []
    for t in temas:
        todos_temas.append(t.toDiccionario())
    return jsonify(todos_temas), 200


@bp_tema.route("/temas/<int:num>", methods = ["GET"])
def temaNumero(num):
    temaBuscado = repo.obtenerPorNumero(num)
    if temaBuscado:
        return jsonify(temaBuscado.toDiccionario()), 200
    else:
        return jsonify({"mensaje": "El tema no fue encontrado"}), 400


@bp_tema.route("/temas", methods = ["POST"])
def nuevoTema():
    if request.is_json:
        datos_tema = request.get_json()
        try:
            nuevo_tema = Tema.fromDiccionario(datos_tema)
            if repo.agregarTema(nuevo_tema):
                return jsonify({"mensaje":"Nuevo tema agregado","nuevo_tema":nuevo_tema.toDiccionario()}), 200
            else:
                return jsonify({"mensaje":"No se pudo agregar"}), 400

        except Exception as e:
            return jsonify({"mensaje": str(e)}), 400
    else:
        return jsonify({"mensaje":"se esperaba datos JSON"})