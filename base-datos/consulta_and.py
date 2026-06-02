from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker
from configuracion import engine
from crear_base_entidades import RecursoAcademico

Session = sessionmaker(bind=engine)
session = Session()


recursos = session.query(RecursoAcademico).filter(
    and_(RecursoAcademico.tipo == 'Guia', RecursoAcademico.fecha_publicacion >= '2024-01-01')
).all()

print("\n GUÍAS PUBLICADAS DE 2024 HACIA ADELANTE ")
for r in recursos:
    print(r)