import random

# --- Build list --- #
numbers = []
while len(numbers) < 8:
    number = random.randint(-100, 100)
    numbers.append(number)
print("Here are some numbers: " + str(numbers))

# --- Print positives --- #
print("These are the positive ones:")

positives = []
for num in numbers:
    if num > 0:
        positives.append(num)
index = 0
while index <= len(positives) - 1:
    print(positives[index])
    index += 1
