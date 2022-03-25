movies = ["Jurassic Park", "Inside Out", "NOVA"]
ranking = []

for movie in movies:
    print(movie)
    rating = input("What is your rating for this movie? ")
    ranking.append(rating)
    
if ranking[0] > ranking[1]:
    if ranking[0] > ranking[2]:
        highest = ranking[0]
        lowest = ranking[1]
    else:
        highest = ranking[2]
        lowest = ranking[2]

if ranking[1] > ranking[2]:
    if ranking[0] > ranking[2]:
        highest = ranking[0]
        lowest = ranking[1]
    else:
        highest = ranking[2]
        lowest = ranking[0]

print(ranking)
print(highest)
print(lowest)
