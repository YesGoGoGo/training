### define the variable cheese and crackers; it's arguments are cheese_count and boxes_of_crackers
# the cheese_count and boxes_of_crackers are just like placeholders for the print statment below; as soon as I feed anything into the function later, then it becomes the value bound to that argument (which is a name, which is a variable?)
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# run the function cheese_and_crackers with the two arguments 20 and 30; note that the 20 will be assigned to the name cheese_count and the boxes_of_crackers will be assigned the number 30
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# define new variables and assign 10 and 50 to them respectively; how the heck does this actually envoke the function?  it looks to me like we are just defining (new) variables, and then all of a sudden it outputs to the console!  ahhhh.... i just looked a little bit lower and now I see what is going on!
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# run the function with the new variables as the arguments; note that these names are different from the names above; i guess this is part of the dynamic type-ness of python; those old arguments are no longer valid?  or, does the function assume the intially defined arguments and look for those only?
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# ok, now the function can accept a mathmatical statment; but will it go back to the orig values if I don't feed it anything?
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# now the function will combine the values from the variables and the math also
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
