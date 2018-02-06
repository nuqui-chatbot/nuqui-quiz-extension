import unittest
from context import nuquiquiz
from sqlalchemy.orm.exc import NoResultFound 
from sqlalchemy.exc import IntegrityError

class TestUser(unittest.TestCase):

    def tearDown(self):
        session = nuquiquiz.SESSION()
        user = session.query(nuquiquiz.User).filter_by(id=0)
        try:
            user.one()
        except NoResultFound:
            print("no user left")
        else:
            nuquiquiz.remove_user(0)

    def test_create_user_works(self):
       session = nuquiquiz.SESSION()
       nuquiquiz.create_user(0, 'testUser')
       user = session.query(nuquiquiz.User).filter_by(id=0).one()
       self.assertEqual(user.id, 0)
       self.assertEqual(user.name, 'testUser')


    def test_remove_user_works(self):
        session = nuquiquiz.SESSION()
        nuquiquiz.create_user(0, 'testUser')
        nuquiquiz.remove_user(0)
        user = session.query(nuquiquiz.User).filter_by(id=0)
        with self.assertRaises(NoResultFound):
            user.one()


    def test_add_meal_work(self):
        session = nuquiquiz.SESSION()
        nuquiquiz.create_user(0, 'testUser')
        food_dict = {
                "apple": {
                    "amount": 1,
                    "calories": 50
                    }
                }
        nuquiquiz.add_meal(0, food_dict)
        user = session.query(nuquiquiz.User).filter_by(id=0).one()
        meal = user.meals[0]
        self.assertEqual(meal.calories, 50)
        self.assertEqual(meal.food, "1 apple")


if __name__ == '__main__':
    unittest.main()
