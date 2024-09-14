from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    user_id = Column(String, unique=True, index=True)
    request_count = Column(Integer, default=0)

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    similarity_score = Column(Float)

# Database setup
DATABASE_URL = "sqlite:///./documents.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
