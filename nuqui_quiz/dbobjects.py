from sqlalchemy import Column, Integer, String, Table, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base

#declare a mapping
global Base
Base = declarative_base()


class Question(Base):
    __tablename__ = 'downloaded_question'

    id = Column(Integer, primary_key=True)
    answer = Column(String)
    question = Column(String)
    value = Column(Integer)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer, ForeignKey('score.id'))

    def to_dictionary(self):
        return {
            "id": self.id,
            "name": self.name,
            "points": self.score.points,
            "last_points": self.score.latest_points
        }


class Score(Base):
    __tablename__ = 'score'

    id = Column(Integer, primary_key=True)
    points = Column(Integer)
    latest_points = Column(Integer)


class Meal(Base):
    __tablename__='meal'

    id = Column(Integer, primary_key=True)
    timestamp = Column(Date)
    calories = Column(Integer)
    food = Column(String)

    def to_dictionary(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "calories": self.calories,
            "food": self.food
        }

