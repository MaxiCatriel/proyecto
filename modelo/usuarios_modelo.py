from app import db, ma, app 
from werkzeug.security import generate_password_hash, check_password_hash



class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'password')
    
usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
