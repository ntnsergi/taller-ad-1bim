from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import Facultad


Session = sessionmaker(bind=engine)
session = Session()


facultades = session.query(Facultad).all()

print("TODAS LAS FACULTADES")
for f in facultades:
    print(f)  