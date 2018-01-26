# a quiz app that tooks the question from http://www.jservice.io/ and put it into the db with https://github.com/nuqui-chatbot/nuqui-question-database
from nuqui_quiz.dbobjects import User
from nuqui_quiz.dbobjects import Score
from nuqui_quiz import SESSION


def create_user(user_id, user_name):
    session = SESSION()
    user_score = Score(points=0, latest_points=0)
    user = User(id=user_id, name=user_name, score=user_score.id)
    session.add(user_score)
    session.add(user)
    session.commit()


def remove_user(user_id):
    session = SESSION()
    user = session.query(User).filter_by(id=user_id).one()
    session.delete(user)
    session.commit()

