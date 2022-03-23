#### ---- SETUP ---- ####

# --- Variables --- #
used_letters = []
last_used_letter = "s"

# --- Print rules --- #
print("Welcome to Word Train! Here are the rules: ")
print("Players take turns entering words. The first letter of each player's word must be the same as the last letter of the previous word. If your word ends with a letter that's already been used, you lose!")

#### ---- GAME LOOP ---- ####
while last_used_letter not in used_letters:
  
    #### ---- PRINT USED LETTERS ---- ####
    used_letters.append(last_used_letter)

    # --- Assemble string of letters --- #
    string_for_used_letters = "Used letters: "
    for used_letter in used_letters:
        used_letters += string_for_used_letters + ", "

    # --- Print string --- #
    print()
    print(string_of_used_letters)

    #### ---- USER INPUT ---- ####

    # --- Get new word --- #
    variable = input("Enter a word beginning with the last used variable: ")

    # --- Get new last letter --- #
    last_used_letter = variable[len(variable) - 1]

#### ---- FINAL OUTPUT ---- ####
print("That letter has already been used. You got " + str(len(used_letters)))
