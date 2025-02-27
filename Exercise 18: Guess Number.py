guess = 0
tries = 0

while guess != 6 and tries < 4:
    tries+=1
    guess = int(input("Guess the number, you have " + str(4 - tries) + " attempts left: "))

if guess == 6:
    print("You got it!")
else:
    print("You ran out of tries!")
