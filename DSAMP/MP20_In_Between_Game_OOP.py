import random

class Card():
    def __init__(self, val):
        self.value = val

    def show(self):
        print("{}".format(self.value))

class Deck():
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for c in range(1, 14):
            self.cards.append(Card(c))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for r in range(len(self.cards)-1, 0, -1):
            i = random.randint(0, r)
            self.cards[r], self.cards[i] = self.cards[i], self.cards[r]

    def draw(self):
        return self.cards.pop()

class Computer():
    def __init__(self):
        self.drawn = []

    def draw(self):
        for i in range(0,2):
            self.drawn.append(Deck.draw())


deck = Deck()
deck.build()
deck.shuffle()
f = deck.draw()
f.show()
deck.build()
deck.shuffle()
s = deck.draw()
s.show()

com = Computer()




