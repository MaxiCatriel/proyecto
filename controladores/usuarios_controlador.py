from app import app, db
from flask import jsonify, request
from modelos.usuarios_modelo import Usuario, usuario_schema, usuarios_schema



@app.route('/registro', methods=['POST'])
def registro_usuario():
    try:
        nombreDeUsuario = request.json['nombreDeUsuario']
        contraseña = request.json['contraseña']
        mail = request.json['mail']

        # Verifica si el nombre de usuario o correo ya existen
        if Usuario.query.filter_by(nombreDeUsuario=nombreDeUsuario).first() is not None:
            return jsonify({"message": "Nombre de usuario ya registrado"}), 400
        if Usuario.query.filter_by(mail=mail).first() is not None:
            return jsonify({"message": "Correo electrónico ya registrado"}), 400

        # Crea un nuevo usuario
        Usuario.create(nombreDeUsuario, contraseña, mail)

        return jsonify({"message": "Usuario registrado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
