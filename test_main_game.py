import unittest
from unittest.mock import patch
from io import StringIO
import main

class TestMainGame(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_welcome(self, mock_stdout):
        main.print_welcome()
        output = mock_stdout.getvalue()
        self.assertIn("Welcome to the RPG", output)
        self.assertIn("Prepare to face the most annoying digital enemies", output)

    @patch('builtins.input', side_effect=['q'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_play_game_quit_immediately(self, mock_stdout, mock_input):

        main.play_game()
        output = mock_stdout.getvalue()
        self.assertIn("Thanks for playing!", output)

    @patch('builtins.input', side_effect=['l', 'q'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_look_and_quit(self, mock_stdout, mock_input):
        main.play_game()
        output = mock_stdout.getvalue()
        self.assertIn("Remaining threats", output)
        self.assertIn("Thanks for playing!", output)

if __name__ == '__main__':
    unittest.main()
