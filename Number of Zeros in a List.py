int_list = [1, 124, 63, 23, 0, 33, 12, 10, 0, 1, 1, 12]
count = 0

#Count Zeroes
for num in int_list:
    if num == 0:
        count += 1

#Final Output
print("List contains " + str(count) + " zeros. ")
