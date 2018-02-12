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
        nuqui.add_meal(0, "wasser,apfel,salz", 200)
        user = session.query(nuqui.User).filter_by(id=0).one()
        meal = user.meals[0]
        self.assertEqual(meal.calories, 200)
        self.assertEqual(meal.food, "wasser,apfel,salz")

        
    def test_get_score(self):
        session = nuqui.SESSION()
        nuqui.create_user(0, 'testUser')
        user = session.query(nuqui.User).filter_by(id=0).one()
        user.score.latest_points = 100
        user.score.points = 100
        session.commit()
        score_dict = nuqui.get_score(0)
        self.assertEqual(score_dict['latest_points'], 100)
        self.assertEqual(score_dict['total_points'], 100)


if __name__ == '__main__':
    unittest.main()
