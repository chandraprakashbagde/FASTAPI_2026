from sqlalchemy import create_engine
DATABASE_url = "sqlite:///./sqllite.db"
engine = create_engine(DATABASE_url, echo=True)