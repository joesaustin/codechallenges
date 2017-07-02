def cards(n):
    suits=["C","D","H","S"]
    numbers=["2","3","4","5","6","7","8","9","0","J","Q","K","A"]
    deck=[]

    for suit in suits:
        #print suit
        for num in numbers:
            deck.append("{}{}".format(num,suit))

    return deck[n]