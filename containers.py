# Exercise 1
students = ["Ada", "Bev", "Cathy"]
print(students[1])
print(students[-1])

# Exercise 2
foods = ("potato", "tater", "fry")
for f in foods:
    print(f"{f} is a good food.")

# Exercise 3
print(foods[1:])

# Exercise 4
home_town = {
    "city": "The Shire",
    "state": "Hobbiton",
    "population": "1,000 hobbits"
}
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

# Exercise 5
for key,val in home_town.items():
    print(f'{key} = {val}')

# Exercise 6
cohort = []
for idx, s in enumerate(students):
    cohortee = {'student': s, 'fav_food': foods[idx]}
    cohort.append(cohortee)
print(cohort)

# Exercise 7
awesome_students = [s + "is awesome!" for s in students]
for s in awesome_students:
    print(s)

# Exercise 8
