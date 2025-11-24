from flask import Blueprint, request, jsonify
from modelos.entidades.prestamos import Prestamo
from modelos.repositorios.repositorios import obtener_repositorio_prestamos


bp_prestamo = Blueprint("rutas_prestamos", __name__)

repo = obtener_repositorio_prestamos()

@bp_prestamo.route('/prestamos', methods = ["GET"])
def todos():
    prestamo = repo.obtenerTodos()
    lista_prestamos_dict = []
    for p in prestamo:
        lista_prestamos_dict.append(p.toDiccioanrio())
    return jsonify(lista_prestamos_dict), 200

@bp_prestamo.route('/prestamos/<int:id>', methods = ["GET"])
def prestamodID(id):
    prestamo = repo.obtenerPrestamoId(id)
    if prestamo:
        return jsonify(prestamo.toDiccionario()), 200
    else:
        return jsonify({'mensaje','El prestamo por es ID no existe'}), 404
    
@bp_prestamo.route('/prestamos/buscar', methods = ['GET'])
def obtenerPrestamo():
    socio_dni = request.args.get('dni')
    libro_isbn = request.args.get('isbn')
    fecha_retiro = request.args.get('fecha_retiro')

    if not socio_dni or not libro_isbn or not fecha_retiro:
        return jsonify({'mensaje': 'Debe proporcionar DNI, ISBN y fecha_retiro para buscar el préstamo.'}), 400
    
    prestamo = repo.obtenerPrestamo(socio_dni, libro_isbn, fecha_retiro)
    if prestamo:
        return jsonify(prestamo.toDiccionario()), 200
    else:
        return jsonify({'mensaje': 'El préstamo con la clave compuesta proporcionada no existe.'}), 404
    
@bp_prestamo.route('/prestamos', methods = ['POST'])
def agregarPrestamo():
    if request.is_json:
        datos_prestmo = request.get_json()
        try:
            nuevo_prestamo = Prestamo.fromDiccionario(datos_prestmo)
            if repo.agregar(nuevo_prestamo):
                return jsonify({'mensaje': 'Nuevo prestamo agregado correctamente', 'prestamo': nuevo_prestamo.toDiccionario()}), 201 
            else:
                return jsonify({'mensaje': 'No se pudo crear el prestamo'}), 404    


        except Exception as e:
            return jsonify({'mensaje': str(e)}), 400
        
@bp_prestamo.route('/prestamos/<int:id>', methods = ['PUT'])
def modificarPrestamo(id):
    try:
        datos_actualizados = request.get_json()

        if datos_actualizados is None:
            return jsonify({'mensaje':'La solicitud debe contener datos JSON'}), 400
        
        prestamo_existente = repo.obtenerPrestamoId(id)
        
        if not prestamo_existente:
            return jsonify({'mensaje':'No se encontro el prestamo'}), 404

        if repo.modificarPorID(id, datos_actualizados):
            return jsonify({
                'mensaje': 'Prestamo actualizado exitosamente',
                'prestamo_actualizado': prestamo_existente.toDiccionario()
            }), 200

        return jsonify({'mensaje':'No se pudo actualizar el prestamo'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@bp_prestamo.route('/prestamos/<int:id>', methods = ['DELETE'])
def eliminarPrestamo(id):
    try:
        prestamo_a_eliminar = repo.obtenerPrestamoId(id)

        if not prestamo_a_eliminar:
                return jsonify({"mensaje": "Prestamo no encontrado"}), 404
        
        if repo.eliminarPorID(id):
            return jsonify({"mensaje": "Prestamo borrado correctamente"}), 200
        else:
            return jsonify({"mensaje": "No se pudo borrar el prestamo"}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400
