#Importamos las librerias 
from flask import render_template, request, redirect,url_for
from conexion import app, db
from models import Alumnos
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

#creamos la ruta principal de nuestra pagina

# @app.route('/')
# def index():
#     return render_template('index.html')

#CRUD - CREAT / CARGAR - READ / MOSTRAR - UPDATE / ACTUALIZAR - DELETE / ELIMINAR

class Materiaform(FlaskForm):
    name = StringField('name')
    submit = SubmitField('submit')

@app.route('/', methods=['GET', 'POST'])
def cargar_materias():
    form = Materiaform()

    if form.validate_on_submit():
        name = request.form['name']

        materia_name = Materia(name)

        db.session.add(materia_name)
        db.session.commit()

    return render_template('index.html', form=form)

@app.route('/cargar_datos', methods = ['GET','POST'])
def cargar_datos():
    #Si el metodo es POST obtenemos los datos 'nombre','apellido' y 'cedula'
    if request.method == 'POST':
        nombre = request.form['nombre']#Eduardo
        apellido = request.form['apellido']#Quinhonez
        cedula = request.form['cedula']

        #Creamos un objeto de la clase Alumnos con los datos obtenidos
        datos_alumnos = Alumnos(nombre, apellido, cedula)

        db.session.add(datos_alumnos)#Agregar a la sesion de la base de datos
        db.session.commit()#Confirmamos la carga de los datos

        return render_template('cargar_datos.html')#Renderizamos la pagina HTML
    
    return render_template('cargar_datos.html')


@app.route('/mostrar_datos',methods = ['GET','POST'])
def mostrar_datos():

    lista_alumnos = Alumnos.query.all()#Creamos el nuevo objeto que contiene la lista total de nuestra base de datos

    return render_template('mostrar_datos.html', lista_alumnos=lista_alumnos)

#Creamos la ruta actualizar donde solicitamos el ID del alumno para mostrar solo ese dato
@app.route('/actualizar/<int:alumno_id>', methods = ['GET', 'POST'])
def actualizar(alumno_id):#Pasamos la variable como parametro a nuestrsa funcion

    alumno_actualizado = Alumnos.query.get(alumno_id)#Creamos un nuevo objeto donde obtenemos los datos de un alumno en especifico

    if request.method == 'POST':#Obtenemos los datos del formulario (nombre,apellido,cedula)
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        cedula = request.form['cedula']

        #Actualizamos los datos obtenidos del formulario instanciando del nuevo objeto
        alumno_actualizado.nombre = nombre
        alumno_actualizado.apellido = apellido
        alumno_actualizado.cedula = cedula

        db.session.commit()#Confirmamos la actualizacion de los datos

        return redirect(url_for('mostrar_datos'))#Redireccionamos a la pagina una vez actualizado los datos.
    
    return render_template ('actualizar.html', alumno_actualizado=alumno_actualizado)

#Creamos la ruta para eliminar... esta ruta no tiene una pagina HTML ya que desde mostrar_datos.html podemos acceder a esta ruta de acuerdo a la configuracion que realizamos en la misma"
@app.route('/eliminar', methods= ['GET', 'POST'])
def eliminar():

    if request.method == 'POST':

        id = request.form['alumno_id'] #Guardamos en la variable id los datos obtenidos del formulario
        alumno_a_eliminar = Alumnos.query.filter_by(id=id).first()#Realizamos la consulta a nuestra base de datos para obtener los datos del alumno en referencia y creamos un nuevo objeto guardando en la variable 

        db.session.delete(alumno_a_eliminar)#Eliminamos los datos del alumno
        db.session.commit()#Confirmamos la eliminacion 

        return redirect(url_for('mostrar_datos'))#Redireccionamos a la pagina para mostrar los datos de la base de datos