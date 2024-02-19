#!/usr/bin/python3
'''
Lists all State objects from the database hbtn_0e_usa
'''
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Lists all the states
    """
    url = 'mysql+mysqldb://{}@localhost/{}'
    engine = create_engine(url.format(sys.argv[1], sys.argv[2], sys.argv[3]),
               pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(state)

    session.close()
