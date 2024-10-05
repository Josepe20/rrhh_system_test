from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Employee(Base):
    __tablename__ = "employees"
    __table_args__ = {"schema": "rrhh"}  # Especifica el esquema

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)

    department_id = Column(Integer, ForeignKey('rrhh.departments.id'))
    job_position_id = Column(Integer, ForeignKey('rrhh.job_positions.id'))

    # Relación con departamentos (Many-to-One)
    department = relationship("Department", back_populates="employees")
    
    # Relación con posiciones de trabajo (Many-to-One)
    job_position = relationship("JobPosition", back_populates="employees")
