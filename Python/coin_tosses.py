import random


def coinToss():
    tail = 0
    head = 0
    print "Starting the program"
    for i in range(1, 5001):
        toss = random.randint(0, 1)  # 0 is head, and 1 is Tail
        if (toss == 0):
            head = head + 1
            what = "head"
        else:
            tail = tail + 1
            what = "tail"
        print "Attempt #", i, ": Throwing a coin... It's a ", what, " ... Got ", head, " head(s) so far and ", tail, "tail(s) so far"
    print "Ending the program, thank you!"
    return

coinToss()
