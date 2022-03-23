gifts = ["four calling birds", "three french hens", "two turtle doves", "a partridge in a pear tree"]
string = ""

count = 0

for gift in gifts:
    string += gift
    if count < 2:
        string += ", "
    elif count == 2:
        string += ", and "
        
    count += 1

print(string)
