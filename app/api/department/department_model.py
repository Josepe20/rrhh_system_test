from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Department(Base):
    __tablename__ = "departments"
    __table_args__ = {"schema": "rrhh"}  # Especifica el esquema

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    status = Column(Boolean, nullable=False)

    # Relación con empleados (One-to-Many)
    employees = relationship("Employee", back_populates="department")

