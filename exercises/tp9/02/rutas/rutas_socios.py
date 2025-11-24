from flask import Blueprint, request, jsonify
from modelos.entidades.socio import Socios
from modelos.repositorios.repositorios import obtener_repositorio_socios

bp_socios = Blueprint("rutas_socio", __name__)

repo = obtener_repositorio_socios()

@bp_socios.route('/socios', methods = ['GET'])
def todos_socios():
    socios = repo.obtener_todos_socios()
    lista_socios_dict = []
    for s in socios:
        lista_socios_dict.append(s.toDiccionario())
    return jsonify (lista_socios_dict), 200

@bp_socios.route('/socios/<int:dni>', methods = ['GET'])
def dni_socios(dni):
    socios = repo.obtener_socio_dni(dni)
    if socios:
        return jsonify(socios.toDiccionario()), 200
    else:
        return jsonify({'mensaje':'Socio no encontrado'}), 404

@bp_socios.route('/socios', methods = ['POST'])
def nuevo_socio():
    if request.is_json:
        datos_socio = request.get_json()
        try:
            nuevo_socio = Socios.fromDiccionario(datos_socio)
            if repo.agregar_nuevo_socio(nuevo_socio):
                return jsonify({'mensaje': 'Nuevo socio agregado correctamente', 
                            'socio_creado': nuevo_socio.toDiccionario()}), 201           
            else:
                return jsonify({'mensaje':'No se pudo agregar socio'}), 404 
        except Exception as e:
            return jsonify({'mensaje':str(e)}), 400

@bp_socios.route('/socios/<int:dni>', methods = ['PUT'])
def actualizar_socio(dni):
    try:
        datos_actualizados = request.get_json()

        if datos_actualizados is None:
            return jsonify({'mensaje':'La solicitud debe contener datos JSON'}), 400
        
        socio_existente = repo.obtener_socio_dni(dni)
        
        if not socio_existente:
            return jsonify({'mensaje':'No se encontro el socio'}), 404

        if repo.modificar_un_socio(dni, datos_actualizados):
            return jsonify({
                'mensaje': 'Socio actualizado exitosamente',
                'socio_actualizado': socio_existente.toDiccionario()
            }), 200

        return jsonify({'mensaje':'No se pudo actualizar el socio'}), 404 
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@bp_socios.route('/socios/<int:dni>', methods = ['DELETE'])
def eliminar_socio(dni):
    try:
        socio_a_eliminar = repo.obtener_socio_dni(dni)

        if not socio_a_eliminar:
                return jsonify({"mensaje": "Socio no encontrado"}), 404
        
        if repo.eliminar_socio(dni):
            return jsonify({"mensaje": "Socio borrado correctamente"}), 200
        else:
            return jsonify({"mensaje": "No se pudo borrar el Socio"}), 404
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 500