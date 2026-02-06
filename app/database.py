import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError

DATABASE_URL = "postgresql://postgres:postgres@db:5432/claimsdb"

# Retry logic for DB connection
for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        engine.connect()
        break
    except OperationalError:
        print("Database not ready, waiting...")
        time.sleep(2)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
