import json
from datetime import datetime
from configuracion import engine
from crear_base_entidades import RecursoAcademico, Profesor
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

with open('data/datos_universidad/datos/recursos_academicos.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)

for d in datos:
    #separacion de nombre y apellido
    nombres, apellidos = d['profesor'].split(' ', 1)
    profesor = session.query(Profesor).filter_by(nombres=nombres, apellidos=apellidos).first()
    
    fecha = datetime.strptime(d['fecha_publicacion'], '%Y-%m-%d').date()
    
    recurso = RecursoAcademico(id=d['id'], titulo=d['titulo'], fecha_publicacion=fecha, 
                               tipo=d['tipo'], url=d['url'], profesor=profesor)
    session.add(recurso)

session.commit()