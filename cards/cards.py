def cards(n):
    s = ["C","D","H","S"]
    d = range(2,10)
    d.extend(["0","J","Q","K","A"])
    deck = []

    for i in s:
        deck.extend(map(lambda x: "{}{}".format(x, i), d))
    return deck[n]

print cards(5)

