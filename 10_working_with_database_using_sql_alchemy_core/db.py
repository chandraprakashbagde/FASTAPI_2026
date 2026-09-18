from sqlalchemy import create_engine

## Install sqlalchemy and create_engine
DATABASE_URL = "sqlite:///./sqlite.db"
engine = create_engine(DATABASE_URL, echo=True)