from flask import Flask
from rutas.rutas_alumnos import bp_alumno
from rutas.rutas_examenes_asignados import bp_examen_asignado
from rutas.rutas_temas import bp_tema

app = Flask(__name__)

app.register_blueprint(bp_alumno)
app.register_blueprint(bp_tema)
app.register_blueprint(bp_examen_asignado)


if __name__ == '__main__':
    app.run(debug=True)