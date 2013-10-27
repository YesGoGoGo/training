# this one is like your scripts with argv
# define the function named print_two and feed it the argument *args


def print_two(*bds):
# define what args will be bound to (i don't know what the astericks does, but I assume that it means something will happen later to define these arguments)
	bd1, bd2 = bds
# output the text below and fill the format characters with arg1 and arg2 respectively
	print "arg1: %r, arg2: %r" % (bd1, bd2)

#ok, that (*args is actually pointless, we can just do this
def print_two_again(bd1, bd2):
	print "arg1: %r, arg2: %r" % (bd1, bd2)

# this just takes one argument
def print_one(bd1):
	print "arg1: %r" % bd1

# this one has no arguments
def print_none():
	print "I got nothin'."

# run these functions with the following arguments:
## the functions won't be run until I get here, where they say print_two; nothing will print above because
print_two("Brian", "Dant")
print_two_again("Brian", "Dant")
print_one("First!")
print_none()
