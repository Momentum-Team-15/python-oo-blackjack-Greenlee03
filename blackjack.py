# Write your blackjack game here.
import random
# outline my classes
SUITS = ['♥️', '♣️', '♦️', '♠️']
RANK_VALUES = {
    'A': (11),
    # TODO handle when A is 1
    'K': 10,
    'Q': 10,
    'J': 10,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10
}


class Game:
#make a new deck of cards, which calls __init__() method
    def __init__(self):
        self.deck =  Deck('Bicycle')
        self.deck.shuffle()
        self.player = player()
        self.dealer = dealer()
        # deal 2 cards to dealer and player
        # self.deal_card(self.dealer)
        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.deal_card(self.player)

        print("The dealer's card is: ")
        for card in self.dealer.hand:
            print(card)
        print(f'Dealer has {self.calculate_hand(self.dealer)}')

        print("The player's cards are: ")
        for card in self.player.hand:
            print(card)
        print(f'Player has {self.calculate_hand(self.player)}')


        print(f'There are now {len(self.deck.cards)} cards in the deck')



    def deal_card(self, participant):
        # take a card from the deck and put it in someone's hand
        card = self.deck.cards.pop()
        participant.hand.append(card)

    def calculate_hand(self, participant):
        total_points = 0
        for card in participant.hand:
            total_points += card.value
        return total_points

class Card:
    def __init__(self,suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f'{self.rank} of {self.suit}'

#example of building one card
# queen_of_hearts = Card('♥️', 'Q', '10')
# print(f'{queen_of_hearts} is worth {queen_of_hearts.value}')
#build a whole deck

class Deck:
    def __init__(self, brand):
        self.cards = []
        self.brand = brand
        self.used = False
        for suit in SUITS:
            for rank_value in RANK_VALUES.items():
                new_card = Card(suit, rank_value[0], rank_value[1])
                self.cards.append(new_card)

    def __str__(self):
        return f'{self.brand} deck of {len(self.cards)} cards'


    def shuffle(self):
        random.shuffle(self.cards)




class player:
    def __init__(self):
        self.hand = []


class dealer:
    def __init__(self):
        self.hand = []


#instantiates the game, calls the __init__() method
# for card in new_game.deck.cards:
#     print(card)
def play_game():
    if new_game.calculate_hand(new_game.player) == 21:
        print('Player has blackjack!')
        new_game.deal_card(new_game.dealer)
        if new_game.calculate_hand(new_game.dealer) == 21:
            print(f"Its a draw, both have {player_points}")
            return
        else:
            print('Player wins with blackjack!')
            return
    # elif new_game.calculate_hand(new_game.dealer) == 21:
    #     print('Dealer wins with blackjack!')
    #     return

    # Player does not have blackjack
    while len(new_game.dealer.hand) < 2:
        choice = ''
        while choice != 's':
            choice = input("Would you like to (h)it or (s)tay?").lower()
            if choice == 'h':
                new_game.deal_card(new_game.player)
                print(f"Player's hand is: ")
                [print(card) for card in new_game.player.hand]
                print(f'Player has {new_game.calculate_hand(new_game.player)}')
                if new_game.calculate_hand(new_game.player) == 21:
                    print("Player has 21!")
                    choice = 's'
                elif new_game.calculate_hand(new_game.player) > 21:
                    print("Player busts!")
                    return

            elif choice == 's':
                if new_game.calculate_hand(new_game.player) <= 21:
                    print(f"Player stays with {new_game.calculate_hand(new_game.player)}")
                    print(f"Player's hand is: ")
                    [print(card) for card in new_game.player.hand]
                    print(f"Dealers hand is: ")
                    new_game.deal_card(new_game.dealer)
                    [print(card) for card in new_game.dealer.hand]
                    while new_game.calculate_hand(new_game.dealer) < 17:
                        new_game.deal_card(new_game.dealer)
                        print("Dealer hits!")
                        [print(card) for card in new_game.dealer.hand]
                        print(f"Dealer has {new_game.calculate_hand(new_game.dealer)}!")
                        if new_game.calculate_hand(new_game.dealer) > 21:
                            print(f'Dealer busted with {new_game.calculate_hand(new_game.dealer)}!')
                            return
                        else:
                            continue
                        # elif new_game.calculate_hand(new_game.dealer) == 21:
                        #     break
                        # else:
                        #     continue

            else:
                print("Please choose 'h' or 's'" )
    else:
        #determine if player has more points than dealer
        dealer_points = new_game.calculate_hand(new_game.dealer)
        player_points = new_game.calculate_hand(new_game.player)
        if dealer_points > player_points:
            print(f'Dealer wins with {dealer_points}. Player has {player_points}')
        elif player_points > dealer_points:
            print(f'Player wins with {player_points}. Dealer has {dealer_points}')
        else:
            print(f"It's a draw, both have {dealer_points}")

new_game = Game()
play_game()

