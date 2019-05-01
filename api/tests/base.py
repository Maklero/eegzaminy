import sys
from unittest import TestCase, skip
from app import create_app

sys.path.append('/')
from settings import Settings

class BaseTestCase(TestCase):
    pass


class ResourceTestCase(BaseTestCase):

    def setUp(self):
        self.app = create_app(Settings)
        self.app.config['DEBUG'] = False
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_initializing_config(self):
        self.assertEqual(self.app.config['DEBUG'], False)
        self.assertEqual(self.app.config['TESTING'], True)
    
    def tearDown(self):
        pass


class ModelTestCase(BaseTestCase):
    pass