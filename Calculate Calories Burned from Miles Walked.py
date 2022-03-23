#### ---- SETUP ---- ####
week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
miles_per_day = []

#### ---- USER INPUT ---- ####
for day in week:
    miles = input("How many miles did you walk on " + day + "? ")
    miles_per_day.append(float(miles))

#### ---- CALCULATE FITNESS ---- ####

# --- Variables --- #
total_miles = 0
total_calories = 0

# --- Calculate sums --- #
for miles in miles_per_day:
    total_miles += miles
    total_calories += miles * 70

# --- Calculate averages --- #
avg_miles = total_miles / len(week)
avg_cal = total_calories / len(week)

#### ---- OUTPUT ---- ####

# --- Intro --- #
print()
print("FITNESS STATS")
print("----------------------------")

# --- Stats --- #
print("Total miles: " + str(total_miles))
print("Total calories " + str(total_calories))
print("Average miles: " + str(avg_miles))
print("Average calories: " + str(avg_cal))
