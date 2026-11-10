from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Database location 
DATABASE_URL = "sqlite:///./AdmitFlow.db"

# Create Database Engine
engine = create_engine(
    DATABASE_URL, connect_args = {"check_same_thread": False}
)

# Create Database Session

SessionLoacal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)

# Base class for database models
Base = declarative_base()

# Database dependency for FastAPI
def get_db():
    db = SessionLoacal()

    try:
        yield db
    finally:
        db.close()