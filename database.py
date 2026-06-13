from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("postgresql://dhinesh:kxZuocCBPvRiLF7juAuv8Mw5BBFPLOht@dpg-d8mpta7lk1mc7390aq3g-a.singapore-postgres.render.com/tododb_j0ds")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()
