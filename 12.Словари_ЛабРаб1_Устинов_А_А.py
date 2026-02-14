sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20,'Кладовая':22}
num_cameras = {"backyard": 6,  "garage": 2,"driveway":1}

slovar = {'mountain':'orod', 'bread':'bass','friend':'mellon', 'horse':'roch'}

animals_in_zoo = {}
animals_in_zoo['Зебры'] = 8
animals_in_zoo['обезьяны'] = 12
animals_in_zoo['динозавры'] = 0
print(animals_in_zoo)


ser_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
ser_ids.update({'theLooper':138475,'stringQueen':85739 })
print(ser_ids)

scar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress":"Emma Stone", "Animated Feature": "Zootopia"}
scar_winners['Supporting Actress'] = 'Viola Davis'
scar_winners['Best Picture'] = 'Moonlight'
print(scar_winners)

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = {key:value for key, value in zip(drinks, caffeine)}
print(zipped_drinks)

