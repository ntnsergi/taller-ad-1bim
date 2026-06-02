from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Profesor

Session = sessionmaker(bind=engine)
session = Session()


profesores = session.query(Profesor).filter(Profesor.especialidad == 'Ingeniería de Software').all()

print("\n PROFESORES DE IS ")
for p in profesores:
    print(p)