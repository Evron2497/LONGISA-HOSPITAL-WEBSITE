from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Float
from database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(255))
    role = Column(String(20)) # e.g., 'admin', 'doctor', 'patient'

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(Text)

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    dept_id = Column(Integer, ForeignKey('departments.id'))
    specialty = Column(String(100))
    experience_years = Column(Integer)