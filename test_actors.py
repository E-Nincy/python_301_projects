import unittest
from unittest.mock import patch
from actors import Hero, Opponent, WeakOpponent, FinalBossOpponent

class TestActors(unittest.TestCase):

    @patch('random.randint')
    def test_hero_wins_attack(self, mock_randint):
        mock_randint.side_effect = [10, 1]  # Hero roll = 10*5 = 50, Opponent = 1*2 = 2
        hero = Hero("Link", 5)
        opp = Opponent("Bug", 2)
        self.assertTrue(hero.attack(opp))

    @patch('random.randint')
    def test_hero_loses_attack(self, mock_randint):
        mock_randint.side_effect = [1, 10]  # Hero roll = 1*5 = 5, Opponent = 10*3 = 30
        hero = Hero("Zelda", 5)
        opp = Opponent("Firewall", 3)
        self.assertFalse(hero.attack(opp))

    @patch('random.randint')
    def test_weak_opponent_attack(self, mock_randint):
        mock_randint.return_value = 3  # 3 * 1 = 3
        opp = WeakOpponent("Glitch", 1)
        result = opp.attack(Hero("Link", 5))
        self.assertEqual(result, 3)

    @patch('actors.random.random')
    @patch('actors.random.randint')
    def test_final_boss_special_attack(self, mock_randint, mock_random):
        mock_randint.return_value = 10
        mock_random.return_value = 0.1 

        boss = FinalBossOpponent("Clippy", 2, "Popups")
        result = boss.attack(Hero("Link", 5))

        expected = 10 * 2 * 2
        self.assertEqual(result, expected)



    @patch('random.randint')
    @patch('random.random')
    def test_final_boss_normal_attack(self, mock_random, mock_randint):
        mock_randint.return_value = 8  # base = 8 * 2 = 16
        mock_random.return_value = 0.5  # No special
        boss = FinalBossOpponent("Clippy", 2, "Popups")
        result = boss.attack(Hero("Link", 5))
        self.assertEqual(result, 16)

    def test_repr(self):
        opp = Opponent("Lag", 4)
        self.assertEqual(repr(opp), "Lag (level4)")

if __name__ == '__main__':
    unittest.main()
