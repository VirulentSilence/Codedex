gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0
print("Q1) Do you like Dawn or Dusk?")
answer1 = input("1) Dawn\n2) Dusk\n")
if answer1 == "1":
    gryffindor += 1
    ravenclaw += 1
elif answer1 == "2":
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input.")
print("Q2) When I'm dead, I want people to remember me as:")
print("    1) The Good")
print("    2) The Great")
print("    3) The Wise")
print("    4) The Bold")
answer2 = int(input("1, 2, 3, or 4? "))
if answer2 == 1:
    hufflepuff += 2
elif answer2 == 2:
    slytherin += 2
elif answer2 == 3:
    ravenclaw += 2
elif answer2 == 4:
    gryffindor += 2
else:
    print("Wrong input.")
print("Q3) Which kind of instrument most pleases your ear?")
print("    1) The violin")
print("    2) The trumpet")
print("    3) The piano")
print("    4) The drum")
answer3 = int(input("1, 2, 3, or 4? "))
if answer3 == 1:
    slytherin += 4
elif answer3 == 2:
    hufflepuff += 4
elif answer3 == 3:
    ravenclaw += 4
elif answer3 == 4:
    gryffindor += 4
else:
    print("Wrong input.")
print("Your score for Gryffindor is " + str(gryffindor) + ".")
print("Your score for Hufflepuff is " + str(hufflepuff) + ".")
print("Your score for Ravenclaw is " + str(ravenclaw) + ".")
print("Your score for Slytherin is " + str(slytherin) + ".")
if gryffindor > hufflepuff and gryffindor > ravenclaw and gryffindor > slytherin:
    print("You belong in Gryffindor!")
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
    print("You belong in Hufflepuff!")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
    print("You belong in Ravenclaw!")
elif slytherin > gryffindor and slytherin > hufflepuff and slytherin > ravenclaw:
    print("You belong in Slytherin!")
else:
    print("You belong in more than one house!")
