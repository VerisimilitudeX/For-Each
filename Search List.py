sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# --- Print original sentence --- #
print("Here is a sentence:")
output = ""
for word in sentence:
    output += word + " "
print(output)
print()

# --- User input --- #
find = input("Please enter a word to find: ")

# --- Find the word --- #
found = False
for word in sentence:
    if word == find:
        found = True
        break

# --- Print whether it was found --- #
if found:
    print("The word is in the sentence. ")
else:
    print("The word is not in the sentence. ")
