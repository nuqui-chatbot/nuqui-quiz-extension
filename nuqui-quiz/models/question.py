from sqlalchemy import Column, Integer, String

class Question(Base):
    __tablename__ = 'downloaded_question'

    id = Column(Integer, primary_key=true)
    answer = Column(String)
    question = Column(String)
    value = Column(Integer)

