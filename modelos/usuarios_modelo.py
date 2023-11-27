
from app import db, ma
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class Usuario(db.Model):
    # ... (otras columnas)
    
    def set_password(self, password):
        self.contraseña_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.contraseña_hash, password)

    @classmethod
    def create(cls, nombreDeUsuario, contraseña, mail):
        nuevo_usuario = cls(nombreDeUsuario=nombreDeUsuario, mail=mail)
        nuevo_usuario.set_password(contraseña)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return nuevo_usuario
