from app import db, ma, app 


class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    descripcion = db.Column(db.String(150))
    precio = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    imagen = db.Column(db.String(400))

    def __init__(self, nombre, descripcion, precio, stock, imagen):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.imagen = imagen

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'descripcion', 'precio', 'stock', 'imagen')

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)

with app.app_context():
    db.create_all()