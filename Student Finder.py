#### ---- SET UP ---- ####
students = ['John', 'Wick', 'Jason', 'Voorhees', 'Freddy', 'Krueger', 'Keyser', 'Soze', 'Mohinder', 'Singh', 'Pandher']
looking = input("Who are you looking for? ")
found = False

#### ---- SEARCH LOOP ---- ####
for student in students:
    if student == looking:
        found = True
        break

#### ---- OUTPUT ---- ####
if found:
    print("The student was in this class ")
else:
    print("The student was not in the class ")
