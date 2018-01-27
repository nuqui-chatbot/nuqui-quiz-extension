from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from nuqui_quiz.dbobjects import Base, Question

engine = create_engine('sqlite:///nuqui_quiz/nuqui.db')
Base.metadata.bind = engine
SESSION = sessionmaker(bind=engine)
Base.metadata.create_all()
session = SESSION()
QUESTIONS = session.query(Question).all()
session.close()