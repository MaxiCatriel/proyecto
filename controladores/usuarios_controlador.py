from app import app, db
from flask import jsonify, request
from modelos.usuarios_modelo import Usuario, usuario_schema, usuarios_schema

@app.route('/usuarios', methods=['POST'])
def create_usuario():
    try:
        nombreDeUsuario = request.json['nombreDeUsuario']
        contraseña = request.json['contraseña']
        mail = request.json['mail']

        new_usuario = Usuario(nombreDeUsuario=nombreDeUsuario, mail=mail)
        new_usuario.set_password(contraseña)

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
            usuario.mail = request.json['mail']

            # Actualiza la contraseña solo si se proporciona una nueva
            nueva_contraseña = request.json.get('contraseña')
            if nueva_contraseña:
                usuario.set_password(nueva_contraseña)

            db.session.commit()
            return usuario_schema.jsonify(usuario), 200
        else:
            return jsonify({"message": "Usuario no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
