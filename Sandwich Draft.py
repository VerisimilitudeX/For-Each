#### ---- SET UP ---- ####
ingredients = ["chicken", "bacon", "hoagie rolls", "Ranch dressing", "Swiss cheese", "avocado", "lettuce", "cheese"]
first_sandwich = []
second_sandwich = []
player1_turn = True

#### ---- DRAFT LOOP ---- ####
while len(ingredients) > 0:

    # --- Print remaining ingredients --- #
    remaining_ingredients = "The remaining ingredients are: "
    for ingredient in ingredients:
        remaining_ingredients += ingredient + ", "    
    print("Remaining ingredients: " + remaining_ingredients)

    # --- Player 1 turn --- #
    if player1_turn:
        player1ingr = input("Choose an ingredient. ")
        if player1ingr in ingredients:
            ingredients.remove(ingredient)
            first_sandwich.append(ingredient)

    # --- Player 2 turn --- #
    else:
        player2ingr = input("Choose an ingredient. ")
        if player2ingr in ingredients:
            ingredients.remove(player2ingr)
            second_sandwich.append(player2ingr)

    # --- Swap turns --- #
    if player1_turn:
        player1_turn = False
    elif not player1_turn:
        player1_turn = True
    print()

#### ---- FINAL OUTPUT ---- ####

# --- Output heading --- #
print("----------------------------------------------------")
print("FINAL OUTPUT")

# --- Player 1 sandwich --- #
stringforplayer1 = "Player 1's sandwich: "
for ingredient in first_sandwich:
    stringforplayer1 += ingredient + ", "
print(stringforplayer1)

# --- Player 2 sandwich --- #
stringforplayer2 = "Player 2's sandwich: "
for ingredient in second_sandwich:
    stringforplayer2 += ingredient + ", "
print(stringforplayer2)
