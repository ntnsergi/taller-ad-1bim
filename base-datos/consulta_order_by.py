from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Carrera

Session = sessionmaker(bind=engine)
session = Session()


carreras = session.query(Carrera).order_by(Carrera.nombre).all()

print("\n CARRERAS ORDENADAS POR ALFABETO")
for c in carreras:
    print(c)