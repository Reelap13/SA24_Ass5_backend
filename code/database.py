from sqlalchemy import create_engine, MetaData
from databases import Database

DATABASE_URL = "postgresql://postgres:postgres@localhost:5433/postgres"

database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)