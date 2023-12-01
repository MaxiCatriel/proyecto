from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://maximilianovm:prueba1234@maximilianovm.mysql.pythonanywhere-services.com/maximilianovm$proyecto'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

app.config['SQLALCHEMY_BINDS']= 'mysql+pymysql://maximilianovm:prueba1234@maximilianovm.mysql.pythonanywhere-services.com/maximilianovm$usuarios'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


from controlador.producto_controlador import *
from controlador.usuarios_controlador import *

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

"""if __name__ == '__main__':
    app.run(debug=True, port=5000)
"""