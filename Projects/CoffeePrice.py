# Coffee Price Python Project

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+             Welcome           +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")

print("We Serve The Following Coffees:")
print("Espresso")
print("Americano")
print("Latte")
print("Cappuccino")
print("Macchiato")
print("Mocha")
print("Flat White")

print("")

price = 0

coffee = input("What coffee would you like?  ")

print("")

if coffee == "Espresso":
  price = price + 4.00
elif coffee == "Americano":
  price = price + 3.00
elif coffee == "Latte":
  price = price + 5.00
elif coffee == "Cappuccino":
  price = price + 6.00
elif coffee == "Macchiato":
  price = price + 6.00
elif coffee == "Mocha":
  price = price + 5.00
elif coffee == "Flat White":
  price = price + 6.00
else:
  print("Sorry, we don't have that.")
  price = price

print("Your total today will be: $" + str(price))

