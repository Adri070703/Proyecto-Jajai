from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#instancia de la clase flask
app = Flask(__name__)

# configuramos la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializamos nuestra base de datos
db.init_app(app)

## rut LEER
## ruta de landing page 


@app.route('/')
def registrar():

#  # Obtener todos los usuarios de la db
    usuario = Usuario.query.all()

    return render_template('landing.html', usuario=usuario )



# Creamos nuestro modelo de db
class Usuario(db.Model):
    ci = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    apellido = db.Column(db.String(20))
    contrasenha = db.Column(db.String(20))
    edad = db.Column(db.Integer)
    email = db.Column(db.String(20))
    telefono = db.Column(db.Integer)
    

class Crecimiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tema = db.Column(db.String(20))
    descripcion = db.Column(db.String(20))
    link = db.Column(db.String(20))

class Emprendimiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tema = db.Column(db.String(20))
    descripcion = db.Column(db.String(20))
    link = db.Column(db.String(20))


# ruta de loggin   
@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == "GET":
        return render_template("login.html")
        
   
    ci = request.form.get("ci")
    contrasenha = request.form.get("contrasenha")
    
    usuario = Usuario.query.filter_by(ci=ci, contrasenha=contrasenha).first()
    print(usuario)
    if usuario :
        # return "el user existe"
        return render_template('home.html')
    else:
         return "Credenciales invalidas, vuelva a intentarlo"
    


## ruta de crear
@app.route('/crear', methods=['GET','POST'])
def crear():
    if request.method =='POST':

        # Obtener los datos de mi formulario
        ci = request.form.get('ci')
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        contrasenha= request.form.get('contrasenha')
        edad = request.form.get('edad')
        email = request.form.get('email')
        telefono = request.form.get('telefono')

        # Creamos el objeto de tipo alumno
        usuario = Usuario(ci= ci, nombre=nombre, apellido=apellido, contrasenha=contrasenha, edad=edad, email=email, telefono=telefono)

        # Agregamos el objeto a la db
        db.session.add(usuario)

        # Guardamos los cambios
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('registrar.html')

    
##nuestra ruta de home
@app.route('/home')
def home():

    return render_template('home.html')




#ruta de inspiracion
@app.route('/inspiracion')
def inspiracion():

    return render_template('inspiracion.html')

#ruta de perfil 

@app.route('/perfil')
def perfil():
    usuarios = Usuario.query.all()
    ultimo = usuarios[len(usuarios)-1]
    return render_template('perfil.html',ultimo=ultimo)



#ruta de editar

@app.route('/editar/<ci>', methods=['GET', 'POST'])
def editar(ci):
    # Obtenemos el ultimo
    usuarios = Usuario.query.all()
    ultimo = usuarios[len(usuarios)-1]
    # Obtenemos la alumna a modificar
    usuario = Usuario.query.get(ci)

    if request.method == 'POST':


        # Obtenemos los datos del formulario 
        usuario.nombre = request.form.get('nombre') 
        usuario.apellido = request.form.get('apellido')
        usuario.contrasenha = request.form.get('contrasenha')
        usuario.edad = request.form.get('edad') 
        usuario.email = request.form.get('email') 
        usuario.telefono = request.form.get('telefono')

        print(request.form)
        # Guardar los cambios
        db.session.commit()

        return redirect(url_for('perfil'))

    return render_template('editar.html', usuario=usuario, ultimo=ultimo)

@app.route('/crecimiento')
def crecimiento():
    crecimientos = Crecimiento.query.all()
    return render_template('crecimiento.html',crecimiento=crecimientos)
    
    


@app.route('/emprendimiento')
def emprendimiento():
    emprendimiento = Emprendimiento.query.all()
    
    return render_template('emprendimiento.html',emprendimiento=emprendimiento)
    

@app.route('/landing')
def landing():
    
    return render_template('landing.html')


### BREAKPOINT ###
if __name__ == '__main__':
    app.run(debug=True)