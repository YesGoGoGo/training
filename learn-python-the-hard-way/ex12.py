# prompt the user to enter their age
age = raw_input("How old are you? ")
# prompt the user to enter their height
height = raw_input("How tall are you? ")
# use raw_input to prompt the user for their weight
weight = raw_input("How much do you weigh? ")

# output the responses from the user within this string of text
print "So, you're %r old, %r tall, and %r heavy." % (age, height, weight)
