import unittest
from word2number import w2n


class TestW2N(unittest.TestCase):

    def test_positives(self):
        self.assertEqual(w2n.word_to_num("two million three thousand nine hundred and eighty four"), 2003984)
        self.assertEqual(w2n.word_to_num("nineteen"), 19)
        self.assertEqual(w2n.word_to_num("two thousand and nineteen"), 2019)
        self.assertEqual(w2n.word_to_num("two million three thousand and nineteen"), 2003019)
        self.assertEqual(w2n.word_to_num('three billion'), 3000000000)
        self.assertEqual(w2n.word_to_num('three million'), 3000000)
        self.assertEqual(w2n.word_to_num('one hundred twenty three million four hundred fifty six thousand seven hundred and eighty nine')
, 123456789)
        self.assertEqual(w2n.word_to_num('eleven'), 11)
        self.assertEqual(w2n.word_to_num('nineteen billion and nineteen'), 19000000019)
        self.assertEqual(w2n.word_to_num('one hundred and forty two'), 142)
        self.assertEqual(w2n.word_to_num('112'), 112)
        self.assertEqual(w2n.word_to_num('11211234'), 11211234)
        self.assertEqual(w2n.word_to_num('five'), 5)
        self.assertEqual(w2n.word_to_num('two million twenty three thousand and forty nine'), 2023049)
        self.assertEqual(w2n.word_to_num('two point three'), 2.3)
        self.assertEqual(w2n.word_to_num('two million twenty three thousand and forty nine point two three six nine'), 2023049.2369)
        self.assertEqual(w2n.word_to_num('one billion two million twenty three thousand and forty nine point two three six nine'), 1002023049.2369)
        self.assertEqual(w2n.word_to_num('point one'), 0.1)
        self.assertEqual(w2n.word_to_num('point'), 0)
        self.assertEqual(w2n.word_to_num('point nineteen'), 0)

    def test_negatives(self):
        self.assertEqual(w2n.word_to_num('112-'), 'Error: No valid number words found! Please enter a valid number word (eg. two million twenty three thousand and forty nine)')
        self.assertEqual(w2n.word_to_num('-'), 'Error: No valid number words found! Please enter a valid number word (eg. two million twenty three thousand and forty nine)')
        self.assertEqual(w2n.word_to_num('on'), 'Error: No valid number words found! Please enter a valid number word (eg. two million twenty three thousand and forty nine)')
        self.assertEqual(w2n.word_to_num('million million'), 'Error: Redundant number! Please enter a valid number word (eg. two million twenty three thousand and forty nine)')
        self.assertEqual(w2n.word_to_num('three million million'), 'Error: Redundant number! Please enter a valid number word (eg. two million twenty three thousand and forty nine)')
        self.assertEqual(w2n.word_to_num('million four million'), 'Error: Redundant number! Please enter a valid number word (eg. two million twenty three thousand and forty nine)')
        self.assertEqual(w2n.word_to_num('thousand million'), 'Error: Malformed number! Please enter a valid number word (eg. two million twenty three thousand and forty nine)')
        self.assertEqual(w2n.word_to_num('one billion point two million twenty three thousand and forty nine point two three six nine'), 'Error: Redundant number! Please enter a valid number word (eg. two million twenty three thousand and forty nine)')
        self.assertEqual(w2n.word_to_num('seventh point nineteen'), 0)
        self.assertEqual(w2n.word_to_num(112), 'Error: Type is not string! Please enter a valid number word (eg. \'two million twenty three thousand and forty nine\')')

if __name__ == '__main__':
    unittest.main()