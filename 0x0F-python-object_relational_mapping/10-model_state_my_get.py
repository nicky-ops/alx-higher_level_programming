#!/usr/bin/python3
'''
This script prints the first state object from the database hbtn_0e_usa
'''
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    List a state from the database
    """
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(url.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    if len(sys.argv) == 5:
        state = session.query(State).filter(State.name == sys.argv[4]).first()
        if state is not None:
            print('{0}'.format(state.id))
        else:
            print("Not Found")

    session.close()
