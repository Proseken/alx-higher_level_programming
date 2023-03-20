#!/usr/bin/python3
""" a Python file similar to model_state.py
    named model_city.py that contains the class definition of a City
"""

import sys
from model_city import City
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    a, b, c = sys.argv[1], sys.argv[2], sys.argv[3]
    data = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(data.format(a, b, c), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(City, State).join(City, State.id == City.state_id)
    for i in result:
        print(f"{i.State.name}: ({i.City.id}) {i.City.name}")
    session.close()
