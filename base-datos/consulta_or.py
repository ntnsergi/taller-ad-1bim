from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Facultad

Session = sessionmaker(bind=engine)
session = Session()


facultades = session.query(Facultad).filter(
    or_(Facultad.ubicacion == 'Edificio A', Facultad.decano == 'Carlos Andrade')
).all()

print("\n BUSCAR FACULTAD POR EDIFICIO O DECANO")
for f in facultades:
    print(f)