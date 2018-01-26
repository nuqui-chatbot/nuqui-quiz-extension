from sqlalchemy import Column, Integer, String, Table, ForeignKey, Date
from sqlalchemy.orm import relationship



class Question(Base):
    __tablename__ = 'downloaded_questions'

    id = Column(Integer, primary_key=True)
    answer = Column(String)
    question = Column(String)
    value = Column(Integer)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer, ForeignKey('scores.id'))

    def to_dictionary(self):
        return {
            "id": self.id,
            "name": self.name,
            "points": self.score.points,
            "last_points": self.score.latest_points
        }


class Score(Base):
    __tablename__ = 'scores'

    id = Column(Integer, primary_key=True)
    points = Column(Integer)
    latest_points = Column(Integer)


class Meal(Base):
    __tablename__='meals'

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

