import json
from configuracion import engine
from crear_base_entidades import Carrera, Facultad
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

with open('data/datos_universidad/datos/carreras.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)

for d in datos:
    facultad = session.query(Facultad).filter_by(nombre=d['facultad']).first()
    
    carrera = Carrera(id=d['id'], nombre=d['nombre'], codigo=d['codigo'], facultad=facultad)
    session.add(carrera)

session.commit()
print("Insercion completa")