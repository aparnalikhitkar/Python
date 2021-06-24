import random




MINIMUM = 1
MAXIMUM = 9
NUMBER = random.randint(MINIMUM, MAXIMUM)
GUESS = None
ANOTHER = None
TRY = 0
RUNNING = True



print ("Alright...")



while RUNNING:
    GUESS = input("What is your lucky number? ")
    if GUESS.lower() == "exit":
        print ("Bye Bye Thank You.")
        RUNNING = False
    elif int(GUESS) < NUMBER:
        print ("Wrong, too low.")
    elif int(GUESS) > NUMBER:
        print ("Wrong, too high.")
    elif int(GUESS) == NUMBER:
        print ("Yes, that's the one, %s." % str(NUMBER))
    if TRY < 2:
        print ("Impressive, only %s try." % str(TRY))
    elif 2 < TRY < 5:
        print ("Pretty good, %s tries." % str(TRY))
    else:
        print ("Bad, %s tries." % str(TRY))
        RUNNING = False
        TRY += 1