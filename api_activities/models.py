from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///activities.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

base = declarative_base()   # default do sqlAlchemy
base.query = db_session.query_property()

class PatternTest(base):
    __tablename__='Pattern'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), index=True) # A fim de tornar a consulta mais rapida quando a mesma for pelo nome
    age = Column(Integer)

    def __repr__(self):
        return '<Pattern {}>'.format(self.name)