def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b


print "Lets do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(9, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


#  A puzzle for the extra credit, type it in anyway.
print "Start the EX CRED -- press Enter"
raw_input()
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# extra credit: do that function by hand
print 35 + (74 - (18 * (50 / 2)))

now = multiply(age, add(weight, subtract(height, divide(iq, 4))))

print "With my inputs, this formula now calculates to:", now
