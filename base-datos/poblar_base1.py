import json
from configuracion import engine
from crear_base_entidades import Facultad
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

with open('data/datos_universidad/datos/facultades.json', 'r', encoding='utf-8') as f:
    datos = json.load(f)

for d in datos:
    facultad = Facultad(id=d['id'], nombre=d['nombre'], ubicacion=d['ubicacion'], decano=d['decano'])
    session.add(facultad)

session.commit()
print("Insercion completa")