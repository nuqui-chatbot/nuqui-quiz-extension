# a quiz app that tooks the question from http://www.jservice.io/ and put it into the db with https://github.com/nuqui-chatbot/nuqui-question-database
from nuqui_quiz.dbobjects import User, Score, Question, Meal
from nuqui_quiz import SESSION, QUESTIONS
from random import randint, shuffle
import datetime


def create_user(user_id, user_name):
    session = SESSION()
    user_score = Score(points=0, latest_points=0)
    user = User(id=user_id, name=user_name, score=user_score)
    session.add(user_score)
    session.add(user)
    session.commit()


def remove_user(user_id):
    session = SESSION()
    user = session.query(User).filter_by(id=user_id).one()
    session.delete(user)
    session.commit()


def get_predefined_question(user_id):
    # get the questions the user already answered and delete them from the list of all questions
    session = SESSION()
    user = session.query(User).filter_by(id=user_id).one()
    questions_id = user.questions
    possible_questions = [question for question in QUESTIONS if question not in questions_id]
    question = possible_questions[randint(0, len(possible_questions))]
    answers = _create_answers(question)
    answers.append(question.answer)
    shuffle(answers)
    question_dict = question.to_dictionary()
    question_dict['answer'] = answers
    user.questions.append(question)
    session.commit()
    return question_dict


def _create_answers(ori_question):
    other_answers_answer = [question.answer for question in QUESTIONS if question != ori_question]
    return [other_answers_answer[randint(0, len(other_answers_answer))] for x in range(0, 3)]


def evaluate(answer, question_id):
    session=SESSION()
    question = session.query(Question).filter_by(id=question_id).one()
    return question.answer == answer
#ToDo: Calculate new score and return a dictionary containing succes, right answer and achieved points


# food as dict eg:
# {
#    "apple" : {
#        "amount": 1,
#        "calories": 50
#    }
# }
def add_meal(user_id, food_dict):
    session=SESSION()
    transformed_dict = _transform_food_dict_to_string_and_cals(food_dict)
    meal = Meal(timestamp=datetime.datetime.now(), calories=transformed_dict["calories"], food=transformed_dict["food_string"])
    session.add(meal)
    user = session.query(User).filter_by(id=user_id).one()
    user.meals.append(meal)
    session.commit()


def _transform_food_dict_to_string_and_cals(food_dict):
    result_list=[]
    calories= 0
    print(food_dict)
    for key, value in food_dict.items():
        calories+=value["calories"]
        if not result_list:
            result_list.append(str(value["amount"])+ " " + key)
        else:
            result_list.append("," + str(value["amount"])+ " " + key)

    return {
        "calories": calories,
        "food_string": ''.join(result_list)
    }
