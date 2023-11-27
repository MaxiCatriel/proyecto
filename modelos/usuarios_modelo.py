from app import db, ma
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombreDeUsuario = db.Column(db.String(50), unique=True, nullable=False)
    contraseña_hash = db.Column(db.String(100), nullable=False)
    mail = db.Column(db.String(100), unique=True, nullable=False)

    def set_password(self, password):
        self.contraseña_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.contraseña_hash, password)

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombreDeUsuario', 'mail')

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)
