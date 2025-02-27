height = int(input("How tall are you in centimeters? "))
credits = int(input("How many credits do you have? "))

if height >= 137 and credits >= 10:
    print("Enjoy the ride!")
elif height >= 137 and credits < 10:
    print("Sorry, you do not have enough credits.")
elif height < 137 and credits >=10:
    print("Sorry, you are not tall enough.")
else:
    print("Sorry, you are not tall enough and do not have enough credits.") 