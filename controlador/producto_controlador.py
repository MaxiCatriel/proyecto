from app import *
from flask import jsonify, request

from modelo.producto_modelo import *

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