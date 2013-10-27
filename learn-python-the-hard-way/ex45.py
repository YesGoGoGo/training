## Animal is-a object
class Animal(object):
	def leap(self, how_high):
		print "I just leaped %d ft." % how_high

## Dog is-a animal
class Dog(Animal):

	def __init__(self, name):
		## has-a name
		self.name = name

	def woof(self):
		print "I'm a dog that goes woof!"

## Cat is-a animal
class Cat(Animal):

	def __init__(self, name):
		## has-a name
		self.name = name

	def mesh(self):
		return Person()

## Person is-a object
class Person(object):

	def __init__(self, name):
		## has-a name
		self.name = name
		# has-a pet
		self.pet = None
		## has-many friends
		self.friends = [
			'Tom', 'Dick', 'Harry',
			'July', 'Joe', 'Richard',
			'Lydia', 'Mary', 'Gary'
		]

	def append(self, add):
		self.name += add

## Employee is-a person
class Employee(Person):

	def __init__(self, name, salary):
		##
		super(Employee, self).__init__(name)
		## has-a salary
		self.salary = salary
		self.jobs = {
			'Best Job': 'Maid',
			'Worst Job': 'Garbage Man',
			'Favorite Job': 'Trader',
			'Last Job': 'Soccer Coach'
		}

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Salmon
class Halibut(Fish):
	pass

## rover is-a dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan

## frank is-a employee
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()

print mary.name
mary.append(" Mo")
print mary.name

rover.woof()
rover.leap(4)

print frank.name
frank.append(" Dude")
print frank.name
print frank.friends
frank.friends.append("That Guy")
print frank.friends

