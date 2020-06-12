with open('p054_poker.txt', 'r') as file:
    hands = file.readlines()


class Hand:
    def __init__(self, input_hand):

        self.hand = [card.replace('T', '10').replace('J', '11').replace('Q', '12')
                         .replace('K', '13').replace('A', '14') for card in input_hand]
        self.hand.sort(key=lambda x: int(x[:-1]))

        self.values = [int(x[:-1]) for x in self.hand]

        self.consecutive = self.is_consecutive()

        self.same_suit = self.is_same_suit()

    def find_hand_rank(self):
        return max(self.high_card(), self.how_many_of_a_kind(), self.straight(), self.flush(), self.straight_flush(),
                   self.royal_flush())

    def is_consecutive(self):
        return self.values == list(range(min(self.values), max(self.values) + 1))

    def is_same_suit(self):
        suits = [card[-1] for card in self.hand]

        if len(set(suits)) > 1:
            return False

        return True

    def how_many_of_a_kind(self):
        hand_value = 0
        count_unique = []

        for value in set(self.values):
            count = self.values.count(value)
            count_unique.append(count)
            if count > 1:
                hand_value += value
                
        if count_unique.count(2) == 1:
            return 100 + hand_value

        if count_unique.count(2) == 2:
            return 200 + hand_value

        if count_unique.count(3) == 1:
            return 300 + hand_value

        if count_unique.count(3) == 1 and count_unique.count(2) == 1:
            return 600 + hand_value

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
        found_higher = False
        idx = 4
        while not found_higher:
            p1_value = p1.values[idx]
            p2_value = p2.values[idx]
            if p1_value != p2_value:
                greater_value = max(p1_value, p2_value)
                found_higher = True
            else:
                idx -= 1

            if idx < 0:
                print('something is WRONG')
                break

    if p1_value == greater_value:
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








