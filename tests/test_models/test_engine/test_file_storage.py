#!usr/bin/python3
""" file to test file storage """
import unittest
import pep8
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.base_model import BaseModel
import os
from datetime import datetime


def setUpModule():
    pass


def tearDownModule():
    pass


class TestStringMethods(unittest.TestCase):
    def testpep8(self):
        style = pep8.StyleGuide(quiet=True)
        file1 = "models/engine/file_storage.py"
        file2 = "tests/test_models/test_engine/test_file_storage.py"
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
        self.cosito = BaseModel()
        self.juan = FileStorage()
        self.cosito.name = "Holberton"
        self.juan.my_number = 89
        self.juan.juanito = ""

    def tearDown(self):
        pass

    def test_name(self):
        self.assertEqual(self.cosito.name, "Holberton")

    def test_number(self):
        self.assertEqual(self.juan.my_number, 89)

    def test_not_existing(self):
        self.assertNotEqual(self.juan.juanito, "no existe")

    def test_instance(self):
        self.assertIsInstance(self.juan, FileStorage)
        self.assertIsInstance(self.cosito, BaseModel)

    def test_create_file(self):
        self.juan.save()
        self.assertTrue(os.path.isfile("file.json"))
        self.assertTrue(hasattr(self.juan, "save"))
        self.assertTrue(hasattr(self.juan, "__init__"))
        self.assertTrue(hasattr(self.juan, "new"))
        self.assertTrue(hasattr(self.juan, "reload"))
        self.assertTrue(hasattr(self.juan, "all"))

    def test_save(self):
        self.cosito.save()
        storage.reload()
        storage.all()
        self.assertTrue(storage.all(), "Holberton")
        self.assertIsInstance(self.cosito.updated_at, datetime)
        self.assertNotEqual(self.cosito.created_at, self.cosito.updated_at)


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
