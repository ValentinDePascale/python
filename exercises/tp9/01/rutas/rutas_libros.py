from flask import Blueprint, request, jsonify
from modelos.entidades.libro import Libro
from modelos.repositorios.repositorios import obtener_repositorio_libros

bp_libros = Blueprint("rutas_libros", __name__)

repo = obtener_repositorio_libros()

@bp_libros.route('/libros', methods=['GET'])
def obtener_libros():
    libros = repo.obtener_todos()
    lista_libros_dict = []
    for l in libros:
        lista_libros_dict.append(l.toDiccionario())
    return jsonify (lista_libros_dict), 200


@bp_libros.route('/libros/<string:isbn>', methods=['GET'])
def obtener_libro_por_isbn(isbn):
    libro = repo.obtener_libro_isbn(isbn)
    if libro:
        return jsonify(libro.toDiccionario()), 200
    else:
        return jsonify ({"mensaje":"Examen no encontrado"}), 404
    
@bp_libros.route('/libros', methods=['POST'])
def agregar_nuevo_libro():
    if request.is_json:
        datos_libro = request.get_json()
        try:
            nuevo_libro = Libro.fromDiccionario(datos_libro)
            if repo.agregar_libro(nuevo_libro):
                return jsonify({"mensaje": "Libro agregado exitosamente", 
                                "nuevo_libro":nuevo_libro.toDiccionario()}), 201
            else:
                return jsonify({"mensaje": "No se pudo agregar el libro"}), 400
        except Exception as e:
            return jsonify({"mensaje": str(e)}), 400
    else:
        return jsonify({"mensaje": "La solicitud debe ser en formato JSON"}), 400
    

@bp_libros.route('/libros/<string:isbn>', methods=['DELETE'])
def eliminar_libro_por_isbn(isbn):
    try:
        libro = repo.obtener_libro_isbn(isbn)
        if not libro:
            return jsonify({"mensaje": "Libro no encontrado"}), 404
        
        if repo.eliminar_libro_isbn(isbn):
            return jsonify({"mensaje": "Libro borrado correctamente"}), 200
        else:
            return jsonify({"mensaje": "No se pudo borrar el libro"}), 404


    except Exception as e:
        return jsonify({'mensaje':str(e)}), 400