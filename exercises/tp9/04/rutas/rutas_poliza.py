from flask import Blueprint, request , jsonify
from modelos.entidades.polizainmueble import PolizaInmueble
from modelos.entidades.polizainmuebleescolar import PolizaInmuebleEscolar
from modelos.repositorios.repositorios import obtener_repositorio_polizas


bp_poliza = Blueprint("rutas_poliza", __name__)

repo = obtener_repositorio_polizas()


#GET ALL
@bp_poliza.route("/polizas", methods = ["GET"])
def todos():
    polizas = repo.obtenerTodas()
    list_polizas = []
    for p in polizas:
        list_polizas.append(p.toDiccionario())
    return jsonify(list_polizas), 200


#GET INDIVIDUAL NUMERO
@bp_poliza.route("/polizas/<int:num>", methods =["GET"])
def porNumero(num):
    polizaBuscada = repo.obtenerPorNumero(num)
    if polizaBuscada:
        return jsonify(polizaBuscada.toDiccionario()), 200
    else:
        return jsonify({"mensaje":"No se pudo encontrar la Poliza"}), 404

#POST AGREGAR
@bp_poliza.route("/polizas", methods=["POST"])
def agregarPoliza():
    if request.is_json:
        datos_poliza = request.get_json()
        try:
            if datos_poliza.get("cant_personas") is not None:
                nueva_poliza = PolizaInmuebleEscolar.fromDiccionario(datos_poliza)
            else: 
                nueva_poliza = PolizaInmueble.fromDiccionario(datos_poliza)

            
            if repo.agregar(nueva_poliza):
                return jsonify({"mensaje":"Se agrego correctamente la nueva poliza"}), 201
            else:
                return jsonify({"mensaje":"No se pudo agregar la nueva poliza"}), 400

        except Exception as e:
            return jsonify ({"mensaje": str(e)}), 400
        

#PUT MODIFICAR
@bp_poliza.route("/polizas/<int:num>", methods=["PUT"])
def actualizar(num):
    try:
        datos_actualizados = request.get_json()
        if datos_actualizados is None:
                return jsonify({'mensaje':'La solicitud debe contener datos JSON'}), 400

        polizaActualizar = repo.obtenerPorNumero(num)

        if not polizaActualizar:
                return jsonify({'mensaje':'No se encontro la poliza'}), 404
        
        if isinstance(polizaActualizar, PolizaInmuebleEscolar):
            poliza_actualizada = PolizaInmuebleEscolar.fromDiccionario(datos_actualizados)
        else: 
            poliza_actualizada = PolizaInmueble.fromDiccionario(datos_actualizados)
            
        if repo.modificarPorNumero(num, poliza_actualizada):
            return jsonify({"mensaje": "Se modifico correctamente los datos de la Poliza"}), 200
        else:
            return jsonify({"mensaje":"No se pudo modificar la poliza"}), 404
        
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400
    
#DELETE
@bp_poliza.route("/polizas/<int:num>", methods=["DELETE"])
def eliminar(num):
    try:
        polizaEliminar = repo.obtenerPorNumero(num)

        if polizaEliminar:
            if repo.eliminarPorNumero(num):
                return jsonify({"mensaje":"se borro correctamente la poliza"}), 200
            else:
                return jsonify({"mensaje":"No se pudo borrar la poliza"}), 404
    except Exception as e:
        return jsonify({"mensaje": str(e)}), 400
