items = ["hello", 12, True, 5.9, (0, 0)]
string = ""
count = 0

for item in items:
    string += str(item)
    if count < len(items) - 1:
        string += ", "
    count += 1

print(string)
