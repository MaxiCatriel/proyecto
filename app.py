from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://maximilianovm:prueba1234@pythonanywhere.com/maxicatriel'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


with app.app_context():
    if not db.engine.has_table(Producto.__tablename__):
        db.create_all()

    if not db.engine.has_table(Usuario.__tablename__):
        db.create_all()


from controladores.productos_controlador import *
from controladores.usuarios_controlador import *

if __name__ == '__main__':
    app.run(debug=True, port=5000)
