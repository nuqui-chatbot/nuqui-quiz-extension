from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .dbobjects import Base, Question, User, Meal, Score

engine = create_engine('sqlite:///nuquiquiz/nuqui.db')
Base.metadata.bind = engine
SESSION = sessionmaker(bind=engine)
Base.metadata.create_all()
session = SESSION()
QUESTIONS = session.query(Question).all()
session.close()

from .nuqui import remove_user, create_user, add_meal, evaluate, get_predefined_question_dict_with_random_answers
