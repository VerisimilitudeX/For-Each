numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

# Count the numbers with three letters
three_letters = 0

for number in numbers:
    if len(number) == 3:
        three_letters += 1

print(str(three_letters) + " of the numbers from 1 to 10 are written with three letters.")
