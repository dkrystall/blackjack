from blackjack import Blackjack
from gambler import Gambler
from card import Suit, CardFace, Card
from random import shuffle

#spawns a blackjack game with 7 decks.
deck = Blackjack(7)

player = Gambler()
dealer = Gambler()
playing = True

def print_dealt_card(self, card_suit, card_value):
    print("cards")

while (playing):
    print("Enter S to start a new game, or Q to quit")
    main_selection = raw_input()
    main_selection = main_selection.lower()
    dealing = None
    if(main_selection == 's'):
        dealing = True
    else:
        print("Goodbye")
        playing = False
    def split_hand():
        print "hand length is:",len(player.hand)
        first_card = player.hand[0][0]
        second_card = player.hand[0][1]
        player.hand[0] = []
        player.hand[1] = []
        player.hand[0].append(first_card)
        player.hand[1].append(second_card)
        
            
    while (dealing):
        print("game starting")
        print("dealing...")
        player.hand[0].append(deck.deal_card())
        dealer.hand[0].append(deck.deal_card())
        player.hand[0].append(deck.deal_card())

        
        print(Suit(player.hand[0][0].suit), CardFace(player.hand[0][0].value))
        dealer.hand.append(deck.deal_card())
        print(Suit(player.hand[0][1].suit), CardFace(player.hand[0][1].value))
        in_game = True

        def print_hand(hand):
            for card in hand:
                print card

        turn = 0
        while (in_game):
            player.score = 0
            print_hand(player.hand[0])
            for card in player.hand[0]:
                if card.value == 1:
                    player.score += 11
                    if player.score > 21:
                        player.score -= 10
                elif card.value < 10:
                    player.score += card.value
                else: 
                    player.score += 10
            
            print "hand value", player.hand[0][0].value, player.hand[0][1].value, "Score is:", player.score
            if player.score > 21:
                print "Busted!"
                print "House wins"
                player.score = 0
                player.hand[0] = []
                in_game = False
                dealing = False
                break

            if turn == 0:
                if ((10 <= player.hand[0][0].value <= 13 and 10 <= player.hand[0][1].value <= 13) or player.hand[0][0].value == player.hand[0][1].value):
                    selection = raw_input("S - Split, H - Hit, D - Double Down, T - Stand")
                else:
                    selection = raw_input("H - Hit, D - Double Down, T - Stand")
            else:
                selection = raw_input("H - Hit, T - Stand")
            selection = selection.lower()
            if selection == 'h':
                player.hand[0].append(deck.deal_card())
            elif selection == 's':
                split_hand()
                split_play = True
                while(split_play):
                    print "hi"
            elif selection =='d':
                player.hand[0].append(deck.deal_card())
            else:
                print("hi")
            turn += 1
