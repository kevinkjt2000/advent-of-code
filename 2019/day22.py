if __name__ == "__main__":
    shuffles = open("day22.input").read().splitlines()
    deck = list(range(10007))
    # shuffles = ["deal with increment 3"]
    # deck = list(range(10))
    for shuffle in shuffles:
        words = shuffle.split(" ")
        technique = words[0]
        if words[1] == "into":
            technique = "reverse"

        if technique == "cut":
            amount = int(words[-1])
            deck = deck[amount:] + deck[:amount]
        elif technique == "deal":
            amount = int(words[-1])
            cursor = 0
            new_deck = deck.copy()
            for card in deck:
                new_deck[cursor] = card
                cursor = (cursor + amount) % len(deck)
            deck = new_deck
        elif technique == "reverse":
            deck.reverse()
    print(deck.index(2019))
