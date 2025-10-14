ricePrice = 45
sugarPrice = 40
oilPrice = 130

riceBought = 3
sugarBought = 2.5
oilBought = 1.8

riceTotal = ricePrice * riceBought
sugarTotal = sugarPrice * sugarBought
oilTotal = oilPrice * oilBought

print("Total Price of ricce: ",riceTotal)
print("Total price of sugar: ", sugarPrice)
print("Total price of oil: ",oilTotal)

totalBill = riceTotal + sugarTotal + oilTotal
print("Total bill is: ", totalBill)

print("Total bill in integer", int(totalBill))
print("Total bill in string", str(totalBill))
