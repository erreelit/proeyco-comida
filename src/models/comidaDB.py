from utiles.db import db


class articulos(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    valor = db.Column(db.String(100))

    def __init__(self, nombre, valor):

        self.nombre = nombre
        self.valor = valor


class usuarioAD(db.Model):

    id = db.Column(db.Integer,  primary_key=True)

    nombreC = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    ciudad = db.Column(db.String(50))
    telefonoC = db.Column(db.String(50))
    FechaP = db.Column(db.String(50))
    estado=db.Column(db.String(50))
    nombre = db.Column(db.String(100))
    valor = db.Column(db.String(100))


    def __init__(self,nombreC,direccion,ciudad,telefonoC,FechaP,estado,nombre,valor):
        self.nombreC=nombreC
        self.direccion=direccion
        self.ciudad=ciudad
        self.telefonoC=telefonoC
        self.FechaP=FechaP
        self.estado=estado
        self.nombre=nombre
        self.valor=valor

