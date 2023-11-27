from app import *
from flask import jsonify, request

from modelos.productos_modelo import *

# crea los endpoint o rutas (json)
@app.route('/productos',methods=['GET'])
def get_Productos():
    all_productos=Producto.query.all()         # el metodo query.all() lo hereda de db.Model
    result=productos_schema.dump(all_productos)  # el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla




@app.route('/productos/<id>',methods=['GET'])
def get_producto(id):
    producto=Producto.query.get(id)
    return producto_schema.jsonify(producto)   # retorna el JSON de un producto recibido como parametro
@app.route('/productos/<id>',methods=['DELETE'])
def delete_producto(id):
    producto=Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    return producto_schema.jsonify(producto)   # me devuelve un json con el registro eliminado


@app.route('/productos', methods=['POST']) # crea ruta o endpoint
def create_producto():
    #print(request.json)  # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    descripcion=request.json['descripcion']
    precio=request.json['precio']
    stock=request.json['stock']
    imagen=request.json['imagen']
    new_producto=Producto(nombre,descripcion,precio,stock,imagen)
    db.session.add(new_producto)
    db.session.commit()
    return producto_schema.jsonify(new_producto)


@app.route('/productos/<id>' ,methods=['PUT'])
def update_producto(id):
    producto=Producto.query.get(id)
 
    producto.nombre=request.json['nombre']
    producto.descripcion=request.json['descripcion']
    producto.precio=request.json['precio']
    producto.stock=request.json['stock']
    producto.imagen=request.json['imagen']


    db.session.commit()
    return producto_schema.jsonify(producto)
 
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
