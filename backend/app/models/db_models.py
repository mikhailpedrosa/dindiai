from sqlalchemy import Column, Integer, String, Float, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()

class FinancialAnalysis(Base):
    __tablename__ = "financial_analyses"
    
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    receita_total = Column(Float)
    despesa_total = Column(Float)
    saldo_mensal = Column(Float)
    report_text = Column(Text)
    created_at = Column(String) # For simple storage or use DateTime

# Configuração do Engine
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dindiai.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
