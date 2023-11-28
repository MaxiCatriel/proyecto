from app import app, db
from flask import jsonify, request
from modelos.usuarios_modelo import Usuario, usuario_schema, usuarios_schema

# Endpoint para obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    try:
        all_usuarios = Usuario.query.all()
        result = usuarios_schema.dump(all_usuarios)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para obtener un usuario por ID
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

# Endpoint para crear un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def create_usuario():
    try:
        data = request.get_json()
        nuevo_usuario = Usuario(username=data['username'], password=data['password'], email=data['email'])
        db.session.add(nuevo_usuario)
        db.session.commit()
        return usuario_schema.jsonify(nuevo_usuario), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para actualizar un usuario por ID
@app.route('/usuarios/<id>', methods=['PUT'])
def update_usuario(id):
    try:
        usuario = Usuario.query.get(id)
        if usuario:
            data = request.get_json()
            usuario.username = data['username']
            usuario.password = data['password']
            usuario.email = data['email']
            db.session.commit()
            return usuario_schema.jsonify(usuario), 200
        else:
            return jsonify({"message": "Usuario no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para eliminar un usuario por ID
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
