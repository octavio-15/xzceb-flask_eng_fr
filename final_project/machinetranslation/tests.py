import unittest
from translator import english_to_french, french_to_english

class TestToFrench(unittest.TestCase):
    def test_1(self):
        self.assertEqual(english_to_french("hello"), "Bonjour")
        self.assertEqual(english_to_french("pencil"), "Crayon")

class TestToNotFrench(unittest.TestCase):
    def test_1(self):
        self.assertNotEqual(english_to_french("hello"), "Crayon")
        self.assertNotEqual(english_to_french("pencil"), "Bonjour")

class TestToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("bonjour"), "Hello")
        self.assertEqual(french_to_english("crayon"), "Pencil")

class TestToNotEnglish(unittest.TestCase):
    def test_1(self):
        self.assertNotEqual(french_to_english("bonjour"), "Pencil")
        self.assertNotEqual(french_to_english("crayon"), "Hello")

class TestToNull(unittest.TestCase):
    def test1(self):
        self.assertIsNone(english_to_french(""), None)

if __name__ == "__main__":
    unittest.main()
