from app import app, db
from flask import jsonify, request
from modelos.usuarios_modelo import Usuario, usuario_schema, usuarios_schema

@app.route('/usuarios', methods=['GET', 'POST'])
def manage_usuarios():
    if request.method == 'GET':
        try:
            all_usuarios = Usuario.query.all()
            result = usuarios_schema.dump(all_usuarios)
            return jsonify(result), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    elif request.method == 'POST':
        try:
            data = request.get_json()
            nuevo_usuario = Usuario(username=data['username'], password=data['password'], email=data['email'])
            db.session.add(nuevo_usuario)
            db.session.commit()
            return usuario_schema.jsonify(nuevo_usuario), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app.route('/usuarios/<id>', methods=['GET', 'PUT', 'DELETE'])
def manage_usuario(id):
    if request.method == 'GET':
        try:
            usuario = Usuario.query.get(id)
            if usuario:
                return usuario_schema.jsonify(usuario), 200
            else:
                return jsonify({"message": "Usuario no encontrado"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    elif request.method == 'PUT':
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

    elif request.method == 'DELETE':
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
