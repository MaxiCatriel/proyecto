from app import app, db
from flask import jsonify, request
from modelos.productos_modelo import Producto, producto_schema, productos_schema

@app.route('/productos', methods=['GET', 'POST'])
def manage_productos():
    if request.method == 'GET':
        try:
            if 'id' in request.args:
                id = request.args['id']
                producto = Producto.query.get(id)
                if producto:
                    return producto_schema.jsonify(producto), 200
                else:
                    return jsonify({"message": "Producto no encontrado"}), 404
            else:
                all_productos = Producto.query.all()
                result = productos_schema.dump(all_productos)
                return jsonify(result), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    elif request.method == 'POST':
        try:
            data = request.get_json()
            nombre = data['nombre']
            descripcion = data['descripcion']
            precio = data['precio']
            stock = data['stock']
            imagen = data['imagen']
            
            new_producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio, stock=stock, imagen=imagen)
            db.session.add(new_producto)
            db.session.commit()
            return producto_schema.jsonify(new_producto), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app.route('/productos/<id>', methods=['DELETE', 'PUT'])
def modify_producto(id):
    if request.method == 'DELETE':
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

    elif request.method == 'PUT':
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
