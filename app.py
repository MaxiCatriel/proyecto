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

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(150))
    precio = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    imagen = db.Column(db.String(400))

    def __init__(self, nombre, descripcion, precio, stock, imagen):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.imagen = imagen

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'descripcion', 'precio', 'stock', 'imagen')

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)

with app.app_context():
    db.create_all()

@app.route('/productos', methods=['GET'])
def get_productos():
    try:
        all_productos = Producto.query.all()
        result = productos_schema.dump(all_productos)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/productos/<id>', methods=['GET'])
def get_producto(id):
    try:
        producto = Producto.query.get(id)
        if producto:
            return producto_schema.jsonify(producto), 200
        else:
            return jsonify({"message": "Producto no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/productos/<id>', methods=['DELETE'])
def delete_producto(id):
    try:
        producto = Producto.query.get(id)
        if producto:
            db.session.delete(producto)
            db.session.commit()
            return producto_schema.jsonify(producto), 200
        else:
            return jsonify({"message": "Producto no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/productos', methods=['POST'])
def create_producto():
    try:
        nombre = request.json['nombre']
        descripcion = request.json['descripcion']
        precio = request.json['precio']
        stock = request.json['stock']
        imagen = request.json['imagen']
        new_producto = Producto(nombre, descripcion, precio, stock, imagen)
        db.session.add(new_producto)
        db.session.commit()
        return producto_schema.jsonify(new_producto), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/productos/<id>', methods=['PUT'])
def update_producto(id):
    try:
        producto = Producto.query.get(id)
        if producto:
            producto.nombre = request.json['nombre']
            producto.descripcion = request.json['descripcion']
            producto.precio = request.json['precio']
            producto.stock = request.json['stock']
            producto.imagen = request.json['imagen']
            db.session.commit()
            return producto_schema.jsonify(producto), 200
        else:
            return jsonify({"message": "Producto no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

"""if __name__ == '__main__':
    app.run(debug=True, port=5000)
"""