from flask import Flask
from app import db, Usuario, Emprendimiento, Crecimiento


# Instancia de la clase flask
app = Flask('app')

# Configuramos la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

#Crear la base de datos
with app.app_context():
  db.create_all()


with app.app_context():

    # Cargamos los datos de la alumnas
    emprendimiento_1 = Emprendimiento(tema='como empezar a emprender con exito', descripcion='Paola Herrera te da una guia sobre como empezar a emprender, estos tips son infalibles para dar tus primeros pasos', link = 'https://www.youtube.com/embed/iuxNzJ0Qs8w?si=kBQVx8aaR4htXspV')
    emprendimiento_2 = Emprendimiento(tema='marketing digital para emprendimientos', descripcion='Mafe Caicedo nos habla de como crear una estrategia de marketing digital que transforme tu marca en una maquina de ventas', link = 'https://www.youtube.com/embed/30l_LXlgKV8?si=pztnDHK76NIxQ02Q')
    emprendimiento_3 = Emprendimiento(tema='como administrar bien el dinero de tu negocio ', descripcion='Judit Catala brinda herramientas para aprender a administrar correctamente el dinero de tu emprendimiento.', link = 'https://www.youtube.com/embed/ycN6dXNkQjA?si=Vj_27cw_i_g6tt58')
    emprendimiento_4 = Emprendimiento(tema='25 ideas de negocio desde casa', descripcion='Paola Herrera brinda 25 ideas de negocios que puedes emprender desde casa. Util para aquellas mujeres que desean iniciar en el mundo del emprendimiento pero que aun no saben como comenzar', link = 'https://www.youtube.com/embed/P9m_f62UGvc?si=TvtkKKwtI1n8BjVw')
    emprendimiento_5 = Emprendimiento(tema='consejos para mujeres emprendedoras ', descripcion='Ana Victoria Garcia, Marisa Lazo y Andrea Arnau de Shark Tank Mexico nos dan los mejores consejos para lograrlo', link = 'https://www.youtube.com/embed/yxWJDzJzURg?si=pcMiNbfHDcD_Ohfc')
    



    db.session.add(emprendimiento_1)
    db.session.add(emprendimiento_2)
    db.session.add(emprendimiento_3)
    db.session.add(emprendimiento_4)
    db.session.add(emprendimiento_5)
    db.session.commit()


with app.app_context():

      crecimiento_1 = Crecimiento(tema="como volverse programadora en solo meses", descripcion="Tatiana nos explica su crecimiento en la programacion y como hizo para lograr esto", link="https://www.youtube.com/embed/xG5Pwnroq1I?si=PqTeqkDts60nqIC_")
      crecimiento_2 = Crecimiento(tema="Mujeres Digitales. Clase 1. Introducción a la tecnología", descripcion="En este video nos van explicando sobre la tecnologia y lo que abarca", link="https://www.youtube.com/embed/SzPjJM-Me8o?si=9FYVgPsQKnvywOav")
      crecimiento_3 = Crecimiento(tema="Mujeres Digitales. Clase 6. Diseño digital I.", descripcion="Nos va explicando y enseñando sobre el diseño digital, sobre su proceso, composicion, tipos de imagenes y mas", link="https://www.youtube.com/embed/J5TBn2f_Ifc?si=PsKKyX2IHNAbev0d")
      crecimiento_4 = Crecimiento(tema="Nuevo curso completo de computacion 2022. Desde cero hasta lo mas avanzado de Ofimatica e Internet", descripcion="En esta clase aprenderas desde lo basico hasta lo avanzado en el uso del computador. Solo ten paciencia para que puedas ver todos dlos capitulos que tiene este video de 10horas...", link="https://www.youtube.com/embed/dyud7aCLUcs?si=oRAVtaPPAwc_x6Lx")
      crecimiento_5 = Crecimiento(tema="Curso de Word Basico. Tutorial Completo 2022. Empieza desde cero Termina en un nivel avanzado", descripcion="Para quienes quieren aprender a crear documentos desde cero con Microsoft Word 2022. En este video vas aprender todo lo que necesitas para crear documentos con todos los formatos y con todas las inserciones que necesites..", link="https://www.youtube.com/embed/S5wffL3L2K8?si=zwjXdXEMA9KaKiTE")
      


      db.session.add(crecimiento_1)
      db.session.add(crecimiento_2)
      db.session.add(crecimiento_3)
      db.session.add(crecimiento_4)
      db.session.add(crecimiento_5)
      db.session.commit()
  
