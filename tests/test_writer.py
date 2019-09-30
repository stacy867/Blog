import unittest
from app.models import Writer

class WriterModelTest(unittest.TestCase):
    
    def setUp(self):
        self.new_writer = Writer(password ='hello')     
    def test_password_setter(self):
        self.assertTrue(self.new_writer.pass_secure is not None)    

    def test_password_verification(self):
        self.assertTrue(self.new_writer.verify_password('hello'))

         

