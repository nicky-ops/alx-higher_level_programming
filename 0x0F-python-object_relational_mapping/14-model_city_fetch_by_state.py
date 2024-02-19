#!/usr/bin/python3
'''
Lists all City objects from the database hbtn_0e_usa
'''
from model_state import Base, State
from model_city import City
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Lists all the cities
    """
    url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(url.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(City, State).join(State)
    for city, state in results.all():
        print("{0}: ({1}) {2}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
