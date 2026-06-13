from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

# Completely bypass target variable extraction. Direct injection of Cloud Postgres DB
DATABASE_URL = "postgresql://dhinesh:kxZuocCBPvRiLF7juAuv8Mw5BBFPLOht@dpg-d8mpta7lk1mc7390aq3g-a.singapore-postgres.render.com/tododb_j0ds"

# Driver string standardization formatting
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
