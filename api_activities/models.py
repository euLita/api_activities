from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///activities.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()   # default do sqlAlchemy
Base.query = db_session.query_property()

class PeoplesTest(Base):
    __tablename__='peoples' # Nome da tabela no banco de dados
    id = Column(Integer, primary_key=True)
    name = Column(String(100), index=True) #A fim de tornar a consulta mais rapida quando a mesma for pelo nome
    age = Column(Integer)

    def __repr__(self): #Representação do objeto
        return '<People {}>'.format(self.name)

class ActivitiesTest(Base):
        __tablename__='activities'
        id = Column(Integer, primary_key=True)
        name = Column(String(200))
        people_id = Column(Integer, ForeignKey('peoples.id'))   #PeoplesTest
        people = relationship("PeoplesTest")

def init_db():
    Base.metadata.create_all(bind=engine) # create_all ele que vai criar o nosso banco de dados

if __name__ == '__main__':
    init_db()