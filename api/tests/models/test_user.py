from app.models import UserModel
from tests.base import ModelTestCase, skip


class TestUserModel(ModelTestCase):

    def setUp(self):
        self.userModel = UserModel(username='FakeUser', password=UserModel.generate_hash('FakeUser'))

    # @skip('Not implemented.')
    def test_add_user_func(self):

        # TODO: Fix this error ->  RuntimeError: No application found. Either work inside a view function  or push an application context.

        self.assertEqual(self.userModel.add_user(), True)


    @skip('Not implemented.')
    def test_find_by_username_func(self):
        pass

    
    def test_generate_hash_func(self):
        password_hash = self.userModel.generate_hash('test')

        self.assertNotEqual(password_hash, None)
        # print(password_hash)
        self.assertEqual(password_hash[0:15], '$pbkdf2-sha256$')

    

    def test_verify_hash_func(self):
        password_hash = self.userModel.generate_hash('test')
        
        self.assertEqual(self.userModel.verify_hash('test', password_hash), True)
            