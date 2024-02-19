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
    Lists all the states from the database
    """
    url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(url.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).order_by(State.id).first()
    if instance is not None:
        print("{0}: {1}".format(instance.id, instance.name))
    else:
        print("Nothing")

    session.close()
