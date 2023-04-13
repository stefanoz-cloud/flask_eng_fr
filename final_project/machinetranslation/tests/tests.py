'''Test examples for Watson English to French and French to English translation'''
import unittest
from translator import english_to_french, french_to_english

class TestTranslateEnToFr(unittest.TestCase):
    '''Class to test function english_to_french'''
    def test1(self):
        ''' Function to test function english_to_french'''
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Hello"), "Oui")

class TestTranslateFrToEn(unittest.TestCase):
    '''Class to test function french_to_english'''
    def test2(self):
        '''Function to test function french_to_english'''
        self.assertIsNone(french_to_english(None))
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bonjour"), "Yes")

unittest.main()
