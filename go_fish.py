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
