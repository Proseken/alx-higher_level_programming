#!/usr/bin/python3
""" a script that creates the State “California” with the
    City “San Francisco” from the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City

if __name__ == "__main__":
    a, b, c = sys.argv[1], sys.argv[2], sys.argv[3]
    data = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(data.format(a, b, c), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newS = State("California")
    newC = City("San Francisco")
    newS.cities.append(newC)
    session.add(newS)
    session.add(newC)
    session.commit()
    session.close()
