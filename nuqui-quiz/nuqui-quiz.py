# a quiz app that tooks the question from http://www.jservice.io/ and put it into the db with https://github.com/nuqui-chatbot/nuqui-question-database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modules.dbobjects import User
from modules.dbobjects import Score

engine = create_engine('sqlite://questions.db')
Session = sessionmaker(bind=engine)


def create_user(user_id, user_name):
    session = Session()
    user_score = Score(points=0, latest_points=0)
    user = User(id=user_id, name=user_name, score=user_score)
    session.add(user_score)
    session.add(user)
    session.commit()


def remove_user(user_id):
    session = Session()
    user = session.query(User).filter_by(id=id).one()
    session.delete(user)
    session.commit()



