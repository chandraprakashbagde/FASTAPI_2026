from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./sqllite.db";

engine = create_engine(DATABASE_URL, echo=True);