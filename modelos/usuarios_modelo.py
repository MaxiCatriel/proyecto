from app import db, ma

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombreDeUsuario = db.Column(db.String(50), unique=True, nullable=False)
    contraseña = db.Column(db.String(100), nullable=False)
    mail = db.Column(db.String(100), unique=True, nullable=False)

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombreDeUsuario', 'contraseña', 'mail')

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)
