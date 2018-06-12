import os
import time
import unittest
import sys
import b


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.dealer = b.Player('dealer')

    def test_player_name(self):
        self.assertEqual(self.dealer.name, 'dealer')

    def test_player_draw_card(self):
        self.assertTrue(self.dealer.draw_a_card() in
                        ['Ace', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_player_hit(self):
        hand = list(self.dealer.hand)
        self.dealer.hit()
        hit = self.dealer.hand
        self.assertTrue(not isinstance(hand, str))
        self.assertTrue(len(hand) < len(hit))

    def test_scoring_hand(self):
        self.dealer.hand = ['Ace', 1, 10]
        self.assertEqual(self.dealer.score(), 12)


if __name__ == '__main__':
    #unittest.main()
    print('test1', end='\r')
    time.sleep(1)
    print('test2', end='\r')
    print('test3')
    time.sleep(2)
    os.system('cls')
#dealer = b.Player('Dealer')
#player1 = b.Player(input('What is your name?'))
#print(dealer.hand)
#print(dealer.draw_a_card())
#dealer.hit()
#print('Dealer drew a {}'.format(dealer.hand))
#dealer.hit()
#score = b.score(dealer.hand)
#print(score)
