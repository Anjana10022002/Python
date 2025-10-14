import random

apple = 15.5
orange = 20
grape = 10.25

totalVolume = apple + orange + grape
print("Total Volume: ",totalVolume)

totalVolume_int = int(totalVolume)
print("Total Volume (integer): ",totalVolume_int)

totalVolume_string = str(totalVolume)
print("Total Volume (string): ",totalVolume_string)

bonusVolume = totalVolume + random.randrange(5,10)
print("Final volume with bonus: ",bonusVolume)