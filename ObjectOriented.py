#ObjectOriented.py

# @author     : Jonathan Ingram
# Created     : 11/24/2020

class Vehicle ():

	vehicleCount = 0
	def __init__(self, wheels): #string powerSource, int wheels
		print("This is a vehicle\n")
		Vehicle.vehicleCount += 1
		self.wheels = wheels

	def info(self):
		print("Wheels    : " + str(self.wheels))

	def flat_tire(self):
		self.wheels -= 1
		print(str(self.wheels) + " wheels remaining")
		if(self.wheels <= 0):
			print("All of your tires are flat")

	def beep(self):
		print("beep beep")


class Car (Vehicle):

	carCount = 0
	def __init__(self, fuelType, transmission): #string transmition
		print("This is also a car\n")
		super().__init__(4) #initalizes a car as a vehicle having 4 wheels
		self.fuelType = fuelType
		self.transmission = transmission
		Car.carCount += 1

	def info(self):
		print("Wheels    : " + str(self.wheels))
		print("Fuel Type : " + self.fuelType)

class Motorcycle (Vehicle):

	motorcycleCount = 0
	def __init__(self, fuelType, style):
		super().__init__(2) #initalizes a motercycle as a vehicle with 2 wheels
		Motorcycle.motorcycleCount += 1
		self.fuelType = fuelType
		self.style = style
	
	

class Mazda (Car):

	mazdaCount = 0	
	def __init__(self, model): #string model
		print ("This is also a Mazda\n")
		super().__init__('gas', 'automatic') #initalizes a mazda as being an gas-fueled automatic car
		Mazda.mazdaCount += 1
		self.model = model

	def info(self):
		print("Wheels       : " + str(self.wheels))
		print("Fuel Type    : " + self.fuelType)
		print("Transmission : " + self.transmission)
		print("Model        : " + self.model)
		print("\n")

	def beep(self): #overwritting the beep method from the parent class
		print("honk honk")

#Main Loop
if __name__ == "__main__":
	
	car = Car('electric', 'automatic')
	mazda3 = Mazda('mazda3')
	harley = Motorcycle('gas', 'manual')

	print("# of vehicles: " + str(Vehicle.vehicleCount))
	print("# of cars: " + str(car.carCount))
	print("# of mazdas: " + str(mazda3.mazdaCount))
	print("# of motorcycles: " + str(harley.motorcycleCount))
