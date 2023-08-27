from flask_sqlalchemy import SQLAlchemy

#Inicializamos la extension SQLAlchemy

db = SQLAlchemy()

#Definimos una clase que representa una tabla en la base de datos
class Alumnos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False )
    apellido = db.Column(db.String(50), nullable=False )
    cedula = db.Column(db.Integer, nullable=False )

    #Constructor de clase
    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula

