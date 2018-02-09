import unittest
from context import nuqui
from sqlalchemy.orm.exc import NoResultFound 
from sqlalchemy.exc import IntegrityError

class TestUser(unittest.TestCase):

    def tearDown(self):
        session = nuqui.SESSION()
        user = session.query(nuqui.User).filter_by(id=0)
        try:
            user.one()
        except NoResultFound:
            print("no user left")
        else:
            nuqui.remove_user(0)

    def test_create_user_works(self):
       session = nuqui.SESSION()
       nuqui.create_user(0, 'testUser')
       user = session.query(nuqui.User).filter_by(id=0).one()
       self.assertEqual(user.id, 0)
       self.assertEqual(user.name, 'testUser')


    def test_remove_user_works(self):
        session = nuqui.SESSION()
        nuqui.create_user(0, 'testUser')
        nuqui.remove_user(0)
        user = session.query(nuqui.User).filter_by(id=0)
        with self.assertRaises(NoResultFound):
            user.one()


    def test_add_meal_work(self):
        session = nuqui.SESSION()
        nuqui.create_user(0, 'testUser')
        food_dict = {
                "apple": {
                    "amount": 1,
                    "calories": 50
                    }
                }
        nuqui.add_meal(0, food_dict)
        user = session.query(nuqui.User).filter_by(id=0).one()
        meal = user.meals[0]
        self.assertEqual(meal.calories, 50)
        self.assertEqual(meal.food, "1 apple")


    def test_evaluate(self):
        session = nuqui.SESSION()
        nuqui.create_user(0, 'testUser')
        user = session.query(nuqui.User).filter_by(id=0).one()
        question = session.query(nuqui.Question).filter_by(id = 156375).one()
        user.open_question = question
        session.commit()
        eval_result = nuqui.evaluate("a shiitake", 0)
        self.assertTrue(eval_result['success'])
        self.assertEqual(eval_result["achieved_points"], 1000)
        self.assertEqual(eval_result["total_points"], 1000)
        self.assertEqual(eval_result["right_answer"], "a shiitake")


if __name__ == '__main__':
    unittest.main()
