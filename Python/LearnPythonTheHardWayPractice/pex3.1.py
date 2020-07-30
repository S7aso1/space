#comeback
from sys import argv
scriptname, cars, spaceincar, drivers, passengers = argv

carsnotdriven = int(cars) - int(drivers)
carsdriven = drivers
carpoolcapacity = int(carsdriven) * int(spaceincar)
avgpass = int(passengers) / int(carsdriven)

print ("there are", cars, "cars available")
print ("there are", drivers, "drivers available")
print ("there are", carsnotdriven, "cars that are free rn")
print ("there is", carpoolcapacity, "car capacity")
print ("there are", passengers, "passengers that need to be transported")
print ("on avarage there are", avgpass, "passangers per car")
