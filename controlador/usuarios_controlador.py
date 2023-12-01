from app import *
from flask import jsonify, request

from modelo.usuarios_modelo import *

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    try:
        all_usuarios = Usuario.query.all()
        result = usuarios_schema.dump(all_usuarios)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/usuarios/<id>', methods=['GET'])
def get_usuario(id):
    try:
        usuario = Usuario.query.get(id)
        if usuario:
            return usuario_schema.jsonify(usuario), 200
        else:
            return jsonify({"message": "Usuario no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/usuarios/<id>', methods=['DELETE'])
def delete_usuario(id):
    try:
        usuario = Usuario.query.get(id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return usuario_schema.jsonify(usuario), 200
        else:
            return jsonify({"message": "Usuario no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/usuarios', methods=['POST'])
def create_usuario():
    try:
        email = request.json['email']
        password = request.json['password']
        new_usuario = Usuario(email, password)
        db.session.add(new_usuario)
        db.session.commit()
        return usuario_schema.jsonify(new_usuario), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/usuarios/<id>', methods=['PUT'])
def update_usuario(id):
    try:
        usuario = Usuario.query.get(id)
        if usuario:
            usuario.email = request.json['email']
            usuario.set_password(request.json['password'])
            db.session.commit()
            return usuario_schema.jsonify(usuario), 200
        else:
            return jsonify({"message": "Usuario no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500