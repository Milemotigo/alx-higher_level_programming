#!/usr/bin/python3
'''script that prints the first State object from the database hbtn_0e_6_usa
'''
import sys
from model_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class SomeClass(Base):

    __tablename__ = 'some_table'
    id = Column(Integer, primary_key=True, nullable=True, unique=True)
    name =  Column(String(128), nullable=True, unique=True)

engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2])@localhost/{sys.argv[3]}')

 Create the tables in the database
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print the State objects
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
