#!/usr/bin/python3
"""a script that lists all State objects that
    contain the letter a from the database hbtn_0e_6_usa
"""

import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sqlalchemy

if __name__ == "__main__":
    a, b, c = sys.argv[1], sys.argv[2], sys.argv[3]
    data = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(data.format(a, b, c), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.name.like("%a%")).all()
    for re in result:
        print(f"{re.id}: {re.name}")
    session.close()
