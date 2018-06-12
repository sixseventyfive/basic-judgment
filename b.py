import os
from random import choice
import sys


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_a_card(self):
        self.value = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.card = choice(self.value)
        return self.card

    def hit(self):
        self.hand.append(self.draw_a_card())
        return self.hand

    def score(self):
        values = self.hand
        score = 0
        count = 0
        aces_count = 0
        for i in values:
            if i == 'Ace':
                values[count] = 0
                aces_count += 1
                count += 1
            else:
                count += 1
        try:
            score = sum(values)
        except TypeError:
            score = 0
        for i in range(aces_count):
            if score + 11 > 21:
                score += 1
            else:
                score += 11
        return score


def rules(hand, dealer_hand):
    s = score(hand)
    d = dealer_hand[0]
    # 'Hard'
    if hand[0] != hand[1] and 0 not in hand:
        if s <= 8:
            action = 'Hit'
        elif s == 9:
            if 3 <= d <= 6:
                action = 'double or hit'
            else:
                action = 'Hit'
        elif s == 10 or s == 11:
            if 2 <= d <= 9:
                action = 'double or hit'
            else:
                action = 'Hit'
        elif s == 12:
            if 4 <= d <= 6:
                action = 'Stand'
            else:
                action = 'Hit'
        elif 13 <= s <= 16:
            if 2 <= d <= 6:
                action = 'Stand'
            else:
                action = 'Hit'
        elif 17 <= s <= 21:
            action = 'Stand'
        elif s > 21:
            action = 'Bust'
        else:
            action = 'logic error'
    #'Soft'
    if hand[0] != hand[1] and 0 in hand:
        pass


def printer(txt):
    print(txt, end='r')


if __name__ == '__main__':
    dealer = Player('dealer')
    player = Player(input('What is your name?\n'))
    os.system('cls')
    play = True
    round = 1
    wins = 0
    while play:
        print("Let's Play!")
        print('Round {}'.format(round))
        dealer.hit()
        player.hit()
        player.hit()
        print('dealer draws {}'.format(dealer.hand))
        p_current = print('You have {} ({})'.format(player.hand,
                                                    player.score()))
        p_current
        h = input('Would you like to hit or stand?\n')
        if h[0] == 'H' or h[0] == 'h':
            player.hit()
        os.system('cls')
        print('dealer has {}'.format(dealer.hand))
        p_current
        round += 1
        play = False

#    play = 'y'
#    win = 0
#    draw = 0
#    lose = 0
#    bet = float(input('how much did you want to bet per round?\n$'))
#    while play == 'y':
#        print('test round')
#        player_hand = [pick_a_card(), pick_a_card()]
#        player_score = score(player_hand)
#        dealer_hand = [pick_a_card(), pick_a_card()]
#        dealer_score = score(dealer_hand)
#        print('Your hand is:')
#        print(player_hand)
#        print('Your score is:')
#        print(player_score)
#        #	player_score = 21
#        print('dealer reveals:')
#        print(dealer_hand[0])
#        if player_score == 21:
#            print('Blackjack!')
#            win = 1.5 + win
#            h = 'n'
#        else:
#            while dealer_score < 17:
#                dealer_hand = hit(dealer_hand)
#                dealer_score = score(dealer_hand)
#            h = input('hit?')
#        while h == 'y' and player_score < 21:
#            player_hand = hit(player_hand)
#            player_score = score(player_hand)
#            print('Your hand is:')
#            print(player_hand)
#            print('Your score is:')
#            print(player_score)
#            if player_score > 21:
#                print('Bust!')
#                break
#            h = input('hit?')
#        print('dealer hand is:')
#        print(dealer_hand)
#        print('dealer score is:')
#        print(dealer_score)
#        if player_score < 22 and (player_score > dealer_score
#                                  or dealer_score > 21):
#            print('You win!')
#            win += 1
#        elif player_score == dealer_score and player_score < 22:
#            print('Draw!')
#            draw += 1
#        else:
#            print('You lose!')
#            lose += 1
#        play = input('again?')
#    print('stats from this round:')
#    print('Total Games: {}'.format(int(win) + lose + draw))
#    print('Games won: {}'.format(int(win)))
#    print('Games drawn: {}'.format(draw))
#    print('Games lost: {}'.format(lose))
#    print('percentage lost {}'.format(lose / (int(win) + lose + draw)))
#    print('Money won: {}'.format(bet * win - bet * lose))
#    input('any key to close')
