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
<<<<<<< HEAD
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{} \
            '.format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url)
=======
    url = 'mysql+mysqldb://{}@localhost/{}'
    engine = create_engine(url.format(sys.argv[1], sys.argv[2], sys.argv[3]),
               pool_pre_ping=True)
>>>>>>> parent of d193c39... add the third argument
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print("{0}: {1}".format(instance.id, instance.name))

    session.close()
