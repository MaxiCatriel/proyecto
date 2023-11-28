from app import db, ma, app

# Defino la tabla de usuarios
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

# Crea la tabla de usuarios
with app.app_context():
    db.create_all()

# Define el esquema para la serialización
class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password', 'email')

# Crea instancias de los esquemas
usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)
