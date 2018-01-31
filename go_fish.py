import random
import unittest

# SI 206 Winter 2018
# Homework 2 - Code

##COMMENT YOUR CODE WITH:
# Section Day/Time: Wednesday, 9 AM
# People you worked with:

######### DO NOT CHANGE PROVIDED CODE #########
### Below is the same cards.py code you saw in lecture.
### Scroll down for assignment instructions.
#########

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cards in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)

	def deal(self, hands, cards_per_hand):
		list_hands = []
		for i in range(0, hands):
			cards_in_hands = []
			for card in self.cards:
				for j in range(0, cards_per_hand):
					cards_in_hands.append(card)
			list_hands.append(cards_in_hands)
		return list_hands


class Hand(object):
	def __init__(self, lst_cards):
		self.init_cards = lst_cards

	def add_card(self, card):
		if card not in self.init_cards:
			self.init_cards.append(card)
		else:
			return "This card in hand already"
	def remove_card(self, card):
		if card not in self.init_cards:
			return "This card not in hand"
		else:
			self.init_cards.remove(card)

	def draw(self, deck):
		draw_card = deck.cards[-1]
		self.init_cards.append(draw_card)
		deck.cards.remove(draw_card)
		return

	def find_pairs(self): #if hand has 2 cards with the same rank, remove them
		card_ranks = {}
		for card in self.init_cards:
			if card.rank not in card_ranks:
				card_ranks[card.rank] = 1
			else:
				card_ranks[card.rank] += 1

		for pair in card_ranks.items():
			if pair[1] >= 2:
				for card in self.init_cards:
						if card.rank == pair[0]:
							self.init_cards.remove(card)


def play_war_game(testing=True):
	# Call this with testing = True and it won't print out all the game stuff -- makes it hard to see test results
	player1 = Deck()
	player2 = Deck()

	p1_score = 0
	p2_score = 0

	player1.shuffle()
	player2.shuffle()
	if not testing:
		print("\n*** BEGIN THE GAME ***\n")
	for i in range(52):
		p1_card = player1.pop_card()
		p2_card = player2.pop_card()
		print('p1 rank_num=', p1_card.rank_num, 'p2 rank_num=', p2_card.rank_num)
		if not testing:
			print("Player 1 plays", p1_card,"& Player 2 plays", p2_card)

		if p1_card.rank_num > p2_card.rank_num:

			if not testing:
				print("Player 1 wins a point!")
			p1_score += 1
		elif p1_card.rank_num < p2_card.rank_num:
			if not testing:
				print("Player 2 wins a point!")
			p2_score += 1
		else:
			if not testing:
				print("Tie. Next turn.")

	if p1_score > p2_score:
		return "Player1", p1_score, p2_score
	elif p2_score > p1_score:
		return "Player2", p1_score, p2_score
	else:
		return "Tie", p1_score, p2_score

if __name__ == "__main__":
	result = play_war_game()
	print("""\n\n******\nTOTAL SCORES:\nPlayer 1: {}\nPlayer 2: {}\n\n""".format(result[1],result[2]))
	if result[0] != "Tie":
		print(result[0], "wins")
	else:
		print("TIE!")


######### DO NOT CHANGE CODE ABOVE THIS LINE #########

## You can write any additional debugging/trying stuff out code in this section...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

#########







##**##**##**##@##**##**##**## # DO NOT CHANGE OR DELETE THIS COMMENT LINE -- we use it for grading your file
###############################################

### Write unit tests below this line for the cards code above.

class TestCard(unittest.TestCase):

	# this is a "test"
	def test_create(self):
		card1 = Card()
		self.assertEqual(card1.suit, "Diamonds")
		self.assertEqual(card1.rank, 2)

	def test_rank_12(self):
		card2 = Card(1,12)
		self.assertEqual(card2.rank, "Queen")

	def test_rank_ace(self):
		card3 = Card(0,1)
		self.assertEqual(card3.rank, "Ace")

	def test_rank_3(self):
		card4 = Card(0,3)
		self.assertEqual(card4.rank, 3)

	def test_suit_1(self):
		card5 = Card(1,5)
		self.assertEqual(card5.suit, "Clubs")

	def test_suit_2(self):
		card6 = Card(2,5)
		self.assertEqual(card6.suit, "Hearts")

	def test_suit_names(self):
		card7 = Card(0,1)
		self.assertEqual(card7.suit_names, ["Diamonds","Clubs","Hearts","Spades"])

	def test_str_method1(self):
		card8 = Card(2,7)
		self.assertEqual(card8.__str__(), "7 of Hearts")

	def test_str_method2(self):
		card9 = Card(3,13)
		self.assertEqual(card9.__str__(), "King of Spades")

class TestDeck(unittest.TestCase):

	def test_deck_has_52(self):
		deck1 = Deck()
		self.assertEqual(len(deck1.cards), 52)

	def test_pop_card1(self):
		deck2 = Deck()
		deck2.pop_card()
		self.assertIsInstance(deck2.pop_card(), Card)

	def test_pop_card2(self):
		deck3 = Deck()
		deck3.pop_card()
		self.assertEqual(len(deck3.cards), 51)

	def test_replace_card1(self):
		deck4 = Deck()
		top_card = deck4.cards[-1]
		deck4.pop_card()
		deck4.replace_card(top_card)
		self.assertEqual(len(deck4.cards), 52)

	def test_replace_card2(self):
		deck5 = Deck()
		top_card = deck5.cards[-1]
		deck5.replace_card(top_card)
		self.assertEqual(len(deck5.cards), 52)

	def test_play_war_game(self):
		play_war_game()
		self.assertIsInstance(play_war_game(), tuple)
		self.assertEqual(len(play_war_game()), 3)
		self.assertIsInstance(play_war_game()[0], str)

	def test_shuffle_deck(self): #Testing that the function shuffle works.
	# the order of cards in deck6 should be different after it is shuffled from
	# deck7 as deck7 is not shuffled.
		deck6 = Deck()
		deck7 = Deck()
		deck6.shuffle()
		for card1 in deck6.cards:
			for card2 in deck7.cards:
				self.assertNotEqual(card1, card2)

	def test_sort_cards(self): #Testing that the sort_cards function works
	# Begin by shuffling a deck to randomize it, and then calling sort_cards
	# Can check if the cards are sorted by seeing if the first card of the deck
	# after sorting is the "ace of diamonds" and the last card is the
	# "King of Spades"

		deck8 = Deck()
		deck8.shuffle()
		deck8.sort_cards()
		self.assertEqual(deck8.cards[0].__str__(), "Ace of Diamonds")
		self.assertEqual(deck8.cards[-1].__str__(), "King of Spades")

	def test_deal_cardsSssssss(self):
		deck9 = Deck()
		deck9.deal(4,5)

		self.assertEqual(len(deck9.deal(4,5)),4)

class TestHand(unittest.TestCase):

	def test_hand_init(self):
		card1 = Card(0,1)
		card2 = Card(1,1)
		card3 = Card(2,4)
		card4 = Card(3,13)
		card5 = Card(3,11)
		lst_cards = [card1,card2,card3,card4,card5]

		hand1 = Hand(lst_cards)
		self.assertEqual(hand1.init_cards, lst_cards)

	def test_add_card1(self):
		card1 = Card(0,1)
		card2 = Card(1,1)
		card3 = Card(2,4)
		lst_cards = [card1,card2,card3]

		hand1 = Hand(lst_cards)
		hand1.add_card(Card(3,13))
		self.assertEqual(len(hand1.init_cards), 4)

	def test_add_card2(self):
		card4 = Card(0,1)
		card5 = Card(1,1)
		card6 = Card(2,4)
		lst_cards = [card4,card5,card6]

		hand2 = Hand(lst_cards)
		hand2.add_card(card4)

		self.assertEqual(len(hand2.init_cards), 3)

	def test_remove_card1(self):
		card7 = Card(0,1)
		card8 = Card(1,1)
		card9 = Card(2,4)
		lst_cards = [card7,card8,card9]

		hand3 = Hand(lst_cards)
		hand3.remove_card(card8)

		self.assertEqual(len(hand3.init_cards), 2)

	def test_remove_card2(self):
		card10 = Card(0,1)
		card11 = Card(1,1)
		card12 = Card(2,4)
		card13 = Card(3,11)
		lst_cards = [card10,card11,card12]

		hand4 = Hand(lst_cards)
		hand4.remove_card(card13)
		self.assertEqual(len(hand4.init_cards), 3)

	def test_draw(self):
		deck1 = Deck()
		top_card = deck1.cards[-1]

		card14 = Card(1,1)
		card15 = Card(2,3)
		lst_cards = [card14,card15]

		hand5 = Hand(lst_cards)
		hand5.draw(deck1)

		self.assertEqual(len(hand5.init_cards),3)
		self.assertEqual(hand5.init_cards[2], top_card)

	def test_remove_pairs(self):
		card16 = Card(1,1)
		card17 = Card(2,1)
		card18 = Card(1, 11)
		lst_cards = [card16,card17]
		hand6 = Hand(lst_cards)

		hand6.find_pairs()

		self.assertEqual(len(hand6.init_cards), 1)


















#############
## The following is a line to run all of the tests you include:
if __name__ == "__main__":
	unittest.main(verbosity=2)
## verbosity 2 to see detail about the tests the code fails/passes/etc.
