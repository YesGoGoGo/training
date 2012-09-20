people = 50
cars = 25
buses = 75

# this will evaluate whether the cars number is higher than people number
if cars > people and buses > people and buses == cars:
# if the if evals to true, then the this line will be printed 
	print "We should take the cars."
# if the if evals to false, then the program will look here and eval this statement
elif cars < people and not (cars == buses):
# if the elif above this line evals to true, then this line will bwe printed
	print "We should not take the cars."
# if nieiter of the two above statemetns evals to true, then do the next thing
else: 
# do this if else evals to true (you know to do this because there is a colon after else 
	print "We can't decide."
# eval if buses is greater than cars
if buses > cars:
# if so, print this line
	print "That's too many buses."
# if not, eval if buses is less than cars
elif buses < cars:
# if the elif evals to true, then print this
	print "Maybe we could take the buses."
# if neiter are true, then drop to here and do what the else says
else: 
# if the else evals to true, then print this	
	print "We still can't decide."

# eval if the people number is greater than the buses number  	
if people > buses:
# if the ir returens true, then print this statement
	print "Alright, let's just take the buses."
# if the if evals to false, drop to here and do what the else says after the colon, after 4 indents
else:
	print "Fine, let's stay home then."	
	
# extra credit
# 1. try to guess what elif and else are doing
# a: else is what happens when everything above it evaluates to true; elif is like a secondary if statement.  if the first one doesn't evaluate to true, check this one, if not, then go on
