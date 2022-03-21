# --- User input --- #
numbers = []
number = 0
while True:
    number = input("Enter numbers (done to stop): ")
    if number == "done":
        break
    else:
        numbers.append(int(number))

# --- Count odd numbers --- #
odd_nums = []
for number in numbers:
    if number % 2 == 1:
        odd_nums.append(number)     

# --- Print results --- #
print("Out of " + str(len(numbers)) + " numbers...")

print("Number of odd numbers: " + str(len(odd_nums)))
