import unittest
import pep8
from models.amenity import Amenity
import os
from datetime import datetime


def setUpModule():
    pass


def tearDownModule():
    pass


class TestStringMethods(unittest.TestCase):
    def testpep8(self):
        style = pep8.StyleGuide(quiet=True)
        file1 = "models/amenity.py"
        file2 = "tests/test_models/test_amenity.py"
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
        self.juan = Amenity()
        self.juan.name = "Holberton"
        self.juan.juanito = ""
        self.this_id = self.juan.id

    def tearDown(self):
        pass

    def test_name(self):
        self.assertEqual(self.juan.name, "Holberton")

    def test_id(self):
        self.assertEqual(self.this_id, self.juan.id)

    def test_not_existing(self):
        self.assertNotEqual(self.juan.juanito, "no existe")

    def test_instance(self):
        self.assertIsInstance(self.juan, Amenity)

    def test_create_file(self):
        self.juan.save()
        self.assertTrue(os.path.isfile("file.json"))
        self.assertTrue(hasattr(self.juan, "save"))
        self.assertTrue(hasattr(self.juan, "__init__"))
        self.assertTrue(hasattr(self.juan, "to_dict"))
        self.assertTrue(hasattr(self.juan, "__str__"))

    def test_save(self):
        juani2 = self.juan.updated_at
        self.juan.save()
        self.assertIsInstance(self.juan.updated_at, datetime)
        self.assertTrue(self.juan.updated_at != juani2)

    def test_dict(self):
        juanito2 = self.juan.to_dict()
        self.assertEqual(self.juan.__class__.__name__, "Amenity")
        self.assertIsInstance(juanito2["updated_at"], str)
        self.assertIsInstance(juanito2["id"], str)
        self.assertIsInstance(juanito2["created_at"], str)


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
