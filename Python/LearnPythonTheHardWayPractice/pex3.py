cars = 100
spaceincar = 4.0
drivers = 30
passengers = 90
carsnotdriven = cars - drivers
carsdriven = drivers
carpoolcapacity = carsdriven * spaceincar
avaragepassengers = passengers / carsdriven

print ("there are", cars, "cars available")
print ("there are", drivers, "drivers available")
print ("there are", carsnotdriven, "cars that are free rn")
print ("there is", carpoolcapacity, "car capacity")
print ("there are", passengers, "passengers that need to be transported")
print ("on avarage there are", avaragepassengers, "passangers per car")
