from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Engine represents the core interface to the database
engine = create_engine('sqlite:///TourMerchManagerDB.db', echo=False)   # Create engine. echo=True turns on logging.
Base = declarative_base()  # All of the mapped classes inherit from this
# Need one instance that everything shares.
Base.metadata.create_all(engine)
