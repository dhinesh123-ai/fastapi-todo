from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

# DIRECT CONNECTION APPROACH (Bypassing getenv since we don't use .env in production)
DATABASE_URL = "postgresql://postgres.submqiozqwxirkztzpaz:DhineshVP%401213@aws-1-ap-southeast-1.pooler.supabase.com:6543/postgres"

# Driver string standardization formatting for SQLAlchemy compatibility
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
