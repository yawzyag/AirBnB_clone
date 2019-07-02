import unittest
from os import sys
from console import HBNBCommand
from unittest.mock import create_autospec, patch
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create(self, server=None):
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_create_command(self):
        # Interpreter obj
        cli = self.create()
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertFalse(cli.onecmd('create BaseModel'))
        self.assertTrue(type(fakeOutput.getvalue().strip()) == str)

    def test_help_command(self):
        # Interpreter obj
        cli = self.create()
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertFalse(cli.onecmd('help'))
        self.assertEqual("", fakeOutput.getvalue().strip())

    def test_help_create_command(self):
        # Interpreter obj
        cli = self.create()
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertFalse(cli.onecmd('help create'))
        self.assertTrue(type(fakeOutput.getvalue().strip()) == str)

    def test_all_command(self):
        # Interpreter obj
        cli = self.create()
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertFalse(cli.onecmd('all'))
        self.assertTrue(type(fakeOutput.getvalue().strip()) == str)

    def test_show_command(self):
        # Interpreter obj
        cli = self.create()
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertFalse(cli.onecmd('show BaseModel'))
        self.assertTrue(type(fakeOutput.getvalue().strip()) == str)

    def test_update_command(self):
        # Interpreter obj
        cli = self.create()
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            str1 = 'update BaseModel 49faff9a-6318-451f-87b6-910505c55907'
            str1 += 'first_name "Betty"'
            self.assertFalse(cli.onecmd(str1))
        str1 = "** value missing **"
        self.assertEqual(str1, fakeOutput.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
