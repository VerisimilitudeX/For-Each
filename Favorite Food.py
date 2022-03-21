import random

fav =  ["burger", "pizza", "burrito"] 
choice = random.randint(0, len(fav) - 1)

print("Do you like " + fav[choice] + "?")
answer = input("y/n\n")

if answer == "y":
    print("You have good taste! ")
