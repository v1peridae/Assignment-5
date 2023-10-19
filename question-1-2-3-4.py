farm_animals =["cows", "sheep", "pigs", "horses", "chickens", "goats", "ducks"]
number_animals = len(farm_animals)
farm_animals.pop(3)  
farm_animals.append("donkeys")  
for x in range(number_animals):
  print(farm_animals[x])
