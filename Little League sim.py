def playball(play, hits, runs, strikes):
    if play == "(FB, F)":
        runs += (hits + 1)
        strikes = 0
        hits = 0

    elif play == "(FB, S)":
        strikes += 1

    elif play == "(C, F)":
        strikes += 1

    elif play == "(C, S)":
        hits += 1
        strikes = 0
    return hits, runs, strikes

with open("litleagsub2.txt") as litleag:
    hits, runs, strikes, outs, = 0, 0, 0, 0
    for play in litleag.readline()[1:-2].split("), "):
        hits, runs, strikes = playball(play + ")", hits, runs, strikes)
        if hits == 4:
            runs += 1
            hits = 0
        if strikes == 3:
            outs += 1
            strikes = 0
        if outs == 3:
            break
    print(runs)


