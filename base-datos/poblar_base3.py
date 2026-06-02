import json
from configuracion import engine
from crear_base_entidades import Profesor, Carrera
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

with open('data/datos_universidad/datos/profesores.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)

for d in datos:
    carrera = session.query(Carrera).filter_by(nombre=d['carrera']).first()
    
    prof = Profesor(id=d['id'], nombres=d['nombres'], apellidos=d['apellidos'], 
                    correo=d['correo'], especialidad=d['especialidad'], carrera=carrera)
    session.add(prof)

session.commit()
print("Insercion completa")
