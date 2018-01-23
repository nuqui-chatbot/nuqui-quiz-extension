# a quiz app that tooks the question from http://www.jservice.io/ and put it into the db with https://github.com/nuqui-chatbot/nuqui-question-database
from sqlalchemy import create_engine


engine = create_engine('sqlite://questions.de')

