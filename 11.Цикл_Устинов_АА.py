board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']
for game in board_games:
    print(game)
for sport in sport_games:
    print(sport)


for i in range(5):
    promise = "I will not chew gum in class"
    print(promise)


students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
for i in students_period_B:
    student = students_period_A.append(i)
    print(students_period_A)


dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie'
]
dog_breed_I_want = 'dalmatian'
for i in dog_breeds_available_for_adoption:
    print(i)
    if i == dog_breed_I_want:
        print('У них есть собака, которую я хочу!')
        break

scoops_sold = 0
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
for i in sales_data:
    for z in i:
        scoops_sold += z
print(scoops_sold)


single_digits = [0,1,2,3,4,5,6,7,8,9]
squares = []
cubes = []
for i in single_digits:
    sq = i * i
    squares.append(sq)
    cu = i * i * i
    cubes.append(cu)
print(squares)
print(cubes)