from models import PeoplesTest, db_session
def insert_peoples():
    people = PeoplesTest(name='Raphael', age=29)
    print(people)
    db_session.add(people)
    db_session.commit()

def consultation():
    people = db_session.get(PeoplesTest, 1)
    # people = PeoplesTest()
    print(people)

if __name__ == '__main__':
    # insert_peoples()
    consultation()