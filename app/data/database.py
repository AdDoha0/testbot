import sqlite3 as sq


from sqlalchemy import  Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

# Создание базового класса для декларативного стиля
Base = declarative_base()

# Таблица names_of_allah
class NameOfAllah(Base):
    __tablename__ = 'names_of_allah'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    name_arabic = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    quran_references = Column(Text, nullable=True)

    # Связь с таблицей user_progress
    user_progress = relationship('UserProgress', back_populates='name')

# Таблица user_progress
class UserProgress(Base):
    __tablename__ = 'user_progress'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    name_id = Column(Integer, ForeignKey('names_of_allah.id'), nullable=False)
    progress = Column(Integer, default=0)
    last_reviewed = Column(DateTime, default=datetime.utcnow)
    is_memorized = Column(Boolean, default=False)

    # Связь с таблицей names_of_allah
    name = relationship('NameOfAllah', back_populates='user_progress')
