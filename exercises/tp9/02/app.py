from flask import Flask
from rutas.rutas_socios import bp_socios

app = Flask(__name__)
app.register_blueprint(bp_socios)

if __name__ == '__main__':
    app.run(debug=True)