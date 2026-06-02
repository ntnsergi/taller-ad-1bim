from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import RecursoAcademico, Profesor, Carrera, Facultad

Session = sessionmaker(bind=engine)
session = Session()


recursos = session.query(RecursoAcademico).join(Profesor).join(Carrera).join(Facultad).filter(Facultad.nombre == "Facultad de Ingeniería") \
    .all()

print("\n RECURSOS ACADÉMICOS DE LA FACULTAD DE INGENIERÍA")
print(*recursos, sep='\n')