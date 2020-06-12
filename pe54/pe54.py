with open('p054_poker.txt', 'r') as file:
    hands = file.readlines()


class Hand:
    def __init__(self, input_hand):

        # Changing the letter card values to numbers for easy sorting
        self.hand = [card.replace('T', '10').replace('J', '11').replace('Q', '12')
                         .replace('K', '13').replace('A', '14') for card in input_hand]

        # Sorting using the card value as the key
        self.hand.sort(key=lambda x: int(x[:-1]))

        # Pulling out the values of each card to be used later
        self.values = [int(x[:-1]) for x in self.hand]

        # Checking if the values are consecutive
        self.consecutive = self.values == list(range(min(self.values), max(self.values) + 1))

        # Checking if the cards all the same suit
        self.same_suit = len(set([card[-1] for card in self.hand])) < 1

    def find_hand_rank(self):
        return max(self.high_card(), self.how_many_of_a_kind(), self.straight(), self.flush(), self.straight_flush(),
                   self.royal_flush())

    def how_many_of_a_kind(self):
        hand_value = 0
        count_unique = []

        for value in set(self.values):
            count = self.values.count(value)
            count_unique.append(count)
            if count > 1:
                hand_value += value

        # One Pair
        if count_unique.count(2) == 1:
            return 100 + hand_value

        # Two Pair
        if count_unique.count(2) == 2:
            return 200 + hand_value

        # Three of a kind
        if count_unique.count(3) == 1:
            return 300 + hand_value

        # Three of a kind and a pair (Full House)
        if count_unique.count(3) == 1 and count_unique.count(2) == 1:
            return 600 + hand_value

        # Four of a kind
        if count_unique.count(4) == 1:
            return 700 + hand_value

        return 0

    def high_card(self):
        return int(self.values[4])

    def straight(self):
        if self.consecutive:
            return 400 + sum(self.values)

        return 0

    def flush(self):
        if self.same_suit:
            return 500 + sum(self.values)

        return 0

    def straight_flush(self):
        if self.same_suit and self.consecutive:
            return 800 + sum(self.values)

        return 0

    def royal_flush(self):
        values = [int(x.strip('SHDC')) for x in self.hand]
        if values == list(range(10, 15)) and self.same_suit:
            return 900

        return 0


def decide_winner(p1, p2):
    p1_value = p1.find_hand_rank()
    p2_value = p2.find_hand_rank()
    greater_value = max(p1_value, p2_value)

    if p1_value == p2_value:
        greater_value = max(set(p1.values).symmetric_difference(set(p2.values)))

    if p1_value == greater_value or greater_value in p1.values:
        winner = 'player1'
    else:
        winner = 'player2'

    return winner


win_count = {'player1': 0, 'player2': 0}

for line in hands:
    player1 = Hand(line.split()[:5])
    player2 = Hand(line.split()[5:])
    win_count[decide_winner(player1, player2)] += 1

print(win_count)








