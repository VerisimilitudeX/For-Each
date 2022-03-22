elements = ["fire", "earth", "air", "water", "magnesium", "carbon"]

# --- Setup --- #
output = ""
count = 0
# --- Loop --- #
for element in elements:
    output += str(element)
    if count < len(elements) - 1:
        output += ", "
    count += 1
# --- Print --- #
print(output)
