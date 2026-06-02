from sqlalchemy import create_engine
from configuracion import engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship 

Base = declarative_base()

from sqlalchemy import Column, Integer, String, Date, ForeignKey

class Facultad(Base):
    __tablename__ = 'facultad'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)
    ubicacion = Column(String)
    decano = Column(String)
    
    carreras = relationship('Carrera', back_populates='facultad')
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.ubicacion} - Decano: {self.decano}"

class Carrera(Base):
    __tablename__ = 'carrera'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    codigo = Column(String, unique=True)
    facultad_id = Column(Integer, ForeignKey('facultad.id'))
    
    facultad = relationship('Facultad', back_populates='carreras')
    profesores = relationship('Profesor', back_populates='carrera')
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - Código: {self.codigo} - ID Facultad: {self.facultad_id}"

class Profesor(Base):
    __tablename__ = 'profesor'
    id = Column(Integer, primary_key=True)
    nombres = Column(String)
    apellidos = Column(String)
    correo = Column(String, unique=True)
    especialidad = Column(String)
    carrera_id = Column(Integer, ForeignKey('carrera.id'))
    
    carrera = relationship('Carrera', back_populates='profesores')
    recursos = relationship('RecursoAcademico', back_populates='profesor')
    
    def __str__(self):
        return f"{self.id} - {self.nombres} {self.apellidos} - {self.correo} - Especialidad: {self.especialidad}"

class RecursoAcademico(Base):
    __tablename__ = 'recurso_academico'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    fecha_publicacion = Column(Date)
    tipo = Column(String)
    url = Column(String)
    profesor_id = Column(Integer, ForeignKey('profesor.id'))
    
    profesor = relationship('Profesor', back_populates='recursos')
    
    def __str__(self):
        return f"{self.id} - {self.titulo} - Tipo: {self.tipo} - Fecha: {self.fecha_publicacion}"
    
Base.metadata.create_all(engine)