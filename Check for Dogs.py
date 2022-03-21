# --- User input --- #
pets = []
pet = ""
while pet != "done":
    pet = input("Enter the pets you have (done to finish): ")
    if pet != "done":
        pets.append(pet)

# --- Find and replace --- #
found = False
for check in pets:
    if check == "dog":
        found = True

# --- Print results --- #   
print("Here are your pets:")
print(pets)
if found == True:
    print("You have a dog. ")
