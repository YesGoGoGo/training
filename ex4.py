#define the value of the variable "cars"
cars = 100
#define the value of the variable space_in_a_car
space_in_a_car = 4.0
#define the number of drivers
drivers = 30
#define the number of passengers
passengers = 90
#define the formula for number of cars not driven
cars_not_driven = cars - drivers
#define the formulas for number of cars being driven
cars_driven = drivers
#define the total number of spaces avialalbe in the car
carpool_capacity = cars_driven * space_in_a_car
#define the average number of passengers / car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
