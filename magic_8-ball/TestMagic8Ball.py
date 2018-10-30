import unittest
from unittest.mock import patch
from Magic8Ball import Fortune

class TestListItems(unittest.TestCase):

    def test_length_fates(self):
        expected = 20
        len_fates = len(Fortune.fates)
        self.assertEqual(expected,len_fates)

    def test_item_in_fates(self):
        items = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes - definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful'
]
        for item in items:
            fates_items = Fortune.fates
            self.assertIn(item,fates_items)

    def test_items_same_as_fates(self):
        items = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes - definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful'
]
        items_in_fates = Fortune.fates
        self.assertEqual(items,items_in_fates)


class TestShakeLoop(unittest.TestCase):

    @patch('Magic8Ball.Fortune.get_input', return_value='y')
    def test_shake_yes(self, input):
        self.assertEqual(Fortune.shake_8ball(self), 'Yes Entered')

    @patch('Magic8Ball.Fortune.get_input', return_value='n')
    def test_shake_no(self, input):
        self.assertEqual(Fortune.shake_8ball(self), 'No Entered')

    #@patch('Magic8Ball.Fortune.get_input', return_value='#')
    #def test_shake_invalid(self, input):
    #    self.assertEqual(Fortune.shake_8ball(self), 'Invalid input')

    #def test_give_fate(self):
     #   fates_answers = ['yes','no','maybe','ask later']
     #   your_fate = Fortune.give_fate(self)
     #   self.assertIn(your_fate, fates_answers)


if __name__ == '__main__':
    unittest.main()