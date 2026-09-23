## Create Vertual envoironment
python3 -m venv env

## Install SQLAlchemy package
pip install SQLAlchemy 

## Install Alembic
pip install alembic

## Initialize Alembic into project
alembic init alembic

## Documentation URL
alembic.sqlalchemy.org


### Alembic Commands

# Initialize
alembic init alembic

# Generate migration
alembic revision --autogenerate -m "message"

# Apply migrations
alembic upgrade head

# Current version
alembic current

# Migration history
alembic history

# Undo latest migration
alembic downgrade -1

# Undo everything
alembic downgrade base