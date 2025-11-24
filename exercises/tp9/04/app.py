from flask import Flask
from rutas.rutas_poliza import bp_poliza

app = Flask(__name__)
app.register_blueprint(bp_poliza)


if __name__ == '__main__':
    app.run(debug=True)