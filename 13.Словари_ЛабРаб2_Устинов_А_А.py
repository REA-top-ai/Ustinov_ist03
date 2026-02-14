zodiac_elements = {"energy": 'Not a Zodiac element',"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
#print(zodiac_elements["fire"])

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
key_to_check = "matcha 30"
try:
    print(caffeine_level[key_to_check])
except KeyError:
    print("That key doesn't exist!")

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id = user_ids.get('teraCoder', 100000)
#print(tc_id)
stack_id = user_ids.get('superStackSmash', 100000)
#print(stack_id)

#user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
#num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
#for user in user_ids.keys():
    #print(user)
#for classes in num_exercises.keys():
    #print(classes)

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0
for zna in num_exercises.values():
    total_exercises += zna
print(total_exercises)