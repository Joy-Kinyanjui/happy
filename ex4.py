cars = 100 # the number of cars
space_in_a_car = 4.0 # space for passengers in a car
drivers = 30 # the numbers of drivers available
passengers = 90 #number of passengers
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average-passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", driverss, "drivers available"
print "There will be", cars_not_driven,"empty cars"
print "We have", passengers, "to carpool today."
print "We have to put about", average_passengers_per_car, "in each car."
