from blackjack import Blackjack
from gambler import Gambler
from card import Suit, CardFace, Card
from random import shuffle

# spawns a blackjack game with 7 decks.

deck = Blackjack(7)
player = Gambler()
dealer = Gambler()
playing = True


def print_dealt_card(self, card_suit, card_value):
    print("cards")


def deal_player_card(self):
    for hand in player.hand:
        hand.append(deck.deal_card)


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
        print "hand length is:", len(player.hand)
        first_card = player.hand[0][0]
        second_card = player.hand[0][1]
        player.hand[0] = []
        player.hand.append([])
        player.hand[0].append(first_card)
        player.hand[1].append(second_card)
        player.hand[0].append(deck.deal_card())
        player.hand[1].append(deck.deal_card())
        print "hand length is:", len(player.hand)

    def print_card(card_face, suit):
        card_face_str = str(card_face).split('.')[1].lower()
        suit_str = str(Suit(suit)).split('.')[1].lower()
        return card_face_str + " of " + suit_str+"s"

    while (dealing):

        print("game starting")
        print("dealing...")
        player.hand[0].append(deck.deal_card())
        dealer.hand[0].append(deck.deal_card())
        player.hand[0].append(deck.deal_card())
        dealer.hand[0].append(deck.deal_card())

        suit1 = Suit(player.hand[0][0].suit)
        suit2 = Suit(player.hand[0][1].suit)

        player_card_1 = print_card(
            CardFace(player.hand[0][0].value), Suit(suit1))
        plater_card_2 = print_card(
            CardFace(player.hand[0][1].value), Suit(suit2))

        print "You have a", player_card_1, "and a", plater_card_2
        print "Dealer is showing a "+ print_card(
            CardFace(dealer.hand[0][1].value), Suit(dealer.hand[0][1].suit))

        in_game = True
        player_turn_over = False

        def print_hand(hand):
            for card in hand[0]:
                print card

        turn = 0
        while (in_game):
            player.score = 0
            # print_hand(player.hand[0])
            print "You have: "
            for card in player.hand[0]:
                this_suit = card.suit
                this_card = print_card(CardFace(card.value), Suit(this_suit))
                print this_card
            print "\n"

            for card in player.hand[0]:
                if card.value == 1:
                    player.score += 11
                    if player.score > 21:
                        player.score -= 10
                elif card.value < 10:
                    player.score += card.value
                else:
                    player.score += 10

            print "Score is:", player.score
            if player.score > 21:
                print "Busted!"
                print "House wins"
                dealer.score = 0
                dealer.hand[0] = []
                player.score = 0
                player.hand[0] = []
                in_game = False
                dealing = False
                break

            if turn == 0:
                if ((10 <= player.hand[0][0].value <= 13 and 10 <= player.hand[0][1].value <= 13) or player.hand[0][0].value == player.hand[0][1].value):
                    selection = raw_input(
                        "S - Split, H - Hit, D - Double Down, T - Stand")
                else:
                    if player_turn_over == True:
                        selection = 't'
                        break
                    else:
                        selection = raw_input(
                            "H - Hit, D - Double Down, T - Stand ")
            else:
                selection = raw_input("H - Hit, T - Stand")
                selection = selection.lower()

            if selection == 'h':
                player_dealt_card = deck.deal_card()
                this_suit = player_dealt_card.suit
                player.hand[0].append(player_dealt_card)
                print "You draw a "+ print_card(CardFace(player_dealt_card.value), Suit(this_suit))

            elif selection == 's':
                split_hand()
                split_play = True
                while(split_play):
                    print "Split play entered"
                    break

            elif selection == 'd':
                player.hand[0].append(deck.deal_card())
                player_turn_over = True

            elif selection == 't':
                print "Entering Dealers Turn"
                dealers_turn = True

                while(dealers_turn):
                    dealer.score = 0
                    print "Dealer has: "
                    for card in dealer.hand[0]:
                        this_suit = card.suit
                        this_card = print_card(CardFace(card.value), Suit(this_suit))
                        print this_card
                    #print_hand(dealer.hand[0])
                    print "\n"
                    for card in dealer.hand[0]:
                        if card.value == 1:
                            dealer.score += 11
                            if dealer.score > 21:
                                dealer.score -= 10
                        elif card.value < 10:
                            dealer.score += card.value
                        else:
                            dealer.score += 10
                    
                    if dealer.score < 16 and dealer.score < player.score:
                        print "Dealer hits"
                        dealer_hit_card = deck.deal_card()
                        dealer.hand[0].append(dealer_hit_card)
                        print "Dealer draws a " + print_card(CardFace(dealer_hit_card.value), Suit(dealer_hit_card.suit))
                        print "Dealers score is: " + str(dealer.score)
                    else:
                        print "Dealer has: "
                        for card in dealer.hand[0]:
                            this_suit = card.suit
                            this_card = print_card(CardFace(card.value), Suit(this_suit))
                            print this_card
                        dealers_turn = False
                        print "Dealers score is: " + str(dealer.score)
                        print "Your score is: " + str(player.score)
                        if dealer.score > 21:
                            print "Dealer busts, You win"
                        elif player.score > dealer.score:
                            print "You win"
                        elif player.score == dealer.score:
                            print "It's a draw"
                        else:
                            print "you lose"
                        dealer.score = 0
                        dealer.hand[0] = []
                        player.score = 0
                        player.hand[0] = []
                        in_game = False
                        dealing = False
                        break
            else:
                print("invalid command")
                break
            turn += 1
