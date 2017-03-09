import random
import math
def grade():
    for i in range(0,10):
        score = random.uniform(60.0,100.0) #randint for integers
        score = int(score)
        if (60.0 <= score <= 69.0):
            print "Score:",(score),"; Your grade is D" #or math.ceil(x)
        elif (70.0 <= score <= 79.0):
            print "Score:",(score),"; Your grade is C"
        elif (80.0 <= score <= 89.0):
            print "Score:",(score),"; Your grade is B"
        elif (90.0 <= score <= 100.0):
            print "Score:",(score),"; Your grade is A"
        # if (score in range(60,100)):
        #   print "Score:",score,"; Your grade is D"
        # elif (score in range(70,80)):
        #   print "Score:",score,"; Your grade is C"
        # elif (score in range(80,90)):
        #   print "Score:",score,"; Your grade is B"
        # elif (score in range(90,101)):
        #   print "Score:",score,"; Your grade is A"
    return

grade()
