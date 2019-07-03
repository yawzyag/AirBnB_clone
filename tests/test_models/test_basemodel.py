import unittest
import pep8
from models.base_model import BaseModel
import juanito


def setUpModule():
    pass


def tearDownModule():
    pass


class TestStringMethods(unittest.TestCase):
    def testpep8(self):
        style = pep8.StyleGuide(quiet=True)
        file1 = "models/base_model.py"
        file2 = "tests/test_base.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")


class TestBaseClass(unittest.TestCase):
    """
    Setupclass
    #Test id
    #Test name
    """

    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "Holberton"
        self.my_model.my_number = 89
        self.my_model.juanito = ""
        self.this_id = self.my_model.id
        self.this_created = self.my_model.created_at
        self.this_updated = self.my_model.updated_at

    def tearDown(self):
        pass

    def test_name(self):
        self.assertEqual(self.my_model.name, "Holberton")

    def test_number(self):
        self.assertEqual(self.my_model.my_number, 89)

    def test_id(self):
        self.assertEqual(self.this_id, self.my_model.id)

    def test_created(self):
        self.assertEqual(self.this_created, self.my_model.created_at)

    def test_updated(self):
        self.assertEqual(self.this_updated, self.my_model.updated_at)

    def test_not_existing(self):
        self.assertNotEqual(self.my_model.juanito, "no existe")

    def test_instance(self):
        self.assertIsInstance(self.my_model, BaseModel)


class TestFib(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
