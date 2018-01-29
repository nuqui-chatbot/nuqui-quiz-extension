import unittest
from context import nuqui_quiz
from sqlalchemy.orm.exc import NoResultFound 
from sqlalchemy.exc import IntegrityError

class TestUser(unittest.TestCase):

    def tearDown(self):
        session = nuqui_quiz.SESSION()
        user = session.query(nuqui_quiz.User).filter_by(id=0)
        try:
            user.one()
        except NoResultFound:
            print("no user left")
        else:
            nuqui_quiz.remove_user(0)

    def test_create_user_works(self):
       session = nuqui_quiz.SESSION()
       nuqui_quiz.create_user(0, 'testUser')
       user = session.query(nuqui_quiz.User).filter_by(id=0).one()
       self.assertEqual(user.id, 0)
       self.assertEqual(user.name, 'testUser')


    def test_remove_user_works(self):
        session = nuqui_quiz.SESSION()
        nuqui_quiz.create_user(0, 'testUser')
        nuqui_quiz.remove_user(0)
        user = session.query(nuqui_quiz.User).filter_by(id=0)
        with self.assertRaises(NoResultFound):
            user.one()


    def test_add_meal_work(self):
        session = nuqui_quiz.SESSION()
        nuqui_quiz.create_user(0, 'testUser')
        food_dict = {
                "apple": {
                    "amount": 1,
                    "calories": 50
                    }
                }
        nuqui_quiz.add_meal(0, food_dict)
        user = session.query(nuqui_quiz.User).filter_by(id=0).one()
        meal = user.meals[0]
        self.assertEqual(meal.calories, 50)
        self.assertEqual(meal.food, "1 apple")


if __name__ == '__main__':
    unittest.main()
