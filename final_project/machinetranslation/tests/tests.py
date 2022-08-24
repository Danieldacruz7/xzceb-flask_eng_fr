import unittest
import json

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        french_text = english_to_french("Hello")
        self.assertEqual(french_text, "Bonjour") # test when English text is "Hello", answer is French "Bonjour"

    def test2(self):
        null_test_1 = english_to_french(None)
        self.assertEqual(null_test_1, "Value cannot be empty.") # test when null is given as input the output is "Value cannot be empty."

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self):
        english_text = french_to_english("Bonjour")
        self.assertEqual(english_text, "Hello") # test when French text is "Bonjour", answer is English "Hello"

    def test2(self):
        null_test_2 = french_to_english(None)
        self.assertEqual(null_test_2, "Value cannot be empty.") # test when null is given as input the output is "Value cannot be empty."
        
unittest.main()