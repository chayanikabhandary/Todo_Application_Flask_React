import os
import unittest
import sys
import json
sys.path.insert(0, os.path.abspath(__file__ + "/../.."))
import app
from app import app, db


class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):

        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/testdb'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def register(self, username, email, password):
        return self.app.post(
            '/register',
            data=json.dumps(dict(username=username,
                                 email=email, password=password)),
            content_type='application/json',
            follow_redirects=True
        )

    def login(self, username, email, password):
        return self.app.post(
            '/login',
            data=json.dumps(dict(username=username,
                                 email=email, password=password)),
            content_type='application/json',
            follow_redirects=True
        )

    def logout(self):
        return self.app.get(
            '/logout',
            follow_redirects=True
        )

    def dataPopulate(
        self, task_heading, task_description,
        due_date, created_by, status, created_at
    ):
        return self.app.post(
            '/dataPopulate',
            data=json.dumps(dict(task_heading=task_heading,
                                 task_description=task_description,
                                 due_date=due_date,
                                 created_by=created_by,
                                 status=status,
                                 created_at=created_at)),
            content_type='application/json',
            follow_redirects=True
        )

    def test_valid_user_registration(self):
        response = self.register('x', 'x@gmail.com', 'x')
        self.assertEqual(response.status_code, 200)

    def test_invalid_user_registration_duplicate_email(self):
        response = self.register('y', 'x@gmail.com', 'y')
        self.assertEqual(response.status_code, 200)
        response = self.register('z', 'x@gmail.com', 'z')
        self.assertEqual(response.status_code, 500)

    def test_invalid_user_login_nonexistent_username(self):
        response = self.login('z', 'ab@gmail.com', 'ab')
        self.assertEqual(response.status_code, 200)

    def test_invalid_user_login_wrong_password(self):
        response = self.login('chayanika.b',
                              'chayanika.bhandary@gmail.com', 'ab')
        self.assertEqual(response.status_code, 200)

    def test_valid_user_login(self):
        response = self.login('chayanika.b',
                              'chayanika.bhandary@gmail.com', 'xyz')
        self.assertEqual(response.status_code, 200)

    


if __name__ == "__main__":
    unittest.main()
