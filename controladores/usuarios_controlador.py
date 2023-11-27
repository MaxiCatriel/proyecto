from app import app, db
from flask import jsonify, request
from modelos.usuarios_modelo import Usuario, usuario_schema, usuarios_schema

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

@app.route('/usuarios', methods=['POST'])
def create_usuario():
    try:
        nombreDeUsuario = request.json['nombreDeUsuario']
        contraseña = request.json['contraseña']
        mail = request.json['mail']

        new_usuario = Usuario(nombreDeUsuario=nombreDeUsuario, contraseña=contraseña, mail=mail)
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
            usuario.nombreDeUsuario = request.json['nombreDeUsuario']
            usuario.contraseña = request.json['contraseña']
            usuario.mail = request.json['mail']

            db.session.commit()
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
