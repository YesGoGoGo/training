low = raw_input("What number would you like to start with? ")
high = raw_input("What number would you like to stop at? ")
change = 2
numbers = []

def the_loop(i, e, f):
	while int(i) < int(e):
		print "At the top of the loop within the function, i is %s" % i
		numbers.append(i)

		i = int(i) + int(f)
		print "Numbers now: ", numbers
		print "At the bottom of the loop within the function, i is %s" % i

#def the_for_loop(i):
#	print "Numbers Now: ", i
#	print "The numbers: "
#	for num in i:
#		print num
#
#the_for_loop(numbers)

the_loop(low, high, change)

print "The numbers: "

for num in numbers:
	print num
