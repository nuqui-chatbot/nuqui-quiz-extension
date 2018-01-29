import unittest
from context import nuqui_quiz
from sqlalchemy.orm.exc import NoResultFound 
from sqlalchemy.exc import IntegrityError

class TestUser(unittest.TestCase):

    def test_create_user_works(self):
       session = nuqui_quiz.SESSION()
       nuqui_quiz.create_user(0, 'testUser')
       user = session.query(nuqui_quiz.User).filter_by(id=0).one()
       self.assertEqual(user.id, 0)
       self.assertEqual(user.name, 'testUser')
       session.delete(user)
       session.commit()

    def test_remove_user_works(self):
        session = nuqui_quiz.SESSION()
        nuqui_quiz.create_user(0, 'testUser')
        nuqui_quiz.remove_user(0)
        user = session.query(nuqui_quiz.User).filter_by(id=0)
        with self.assertRaises(NoResultFound):
            user.one()
        


if __name__ == '__main__':
    unittest.main()
