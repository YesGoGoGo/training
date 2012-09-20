# assignment: define a function and run it 10 different ways

def nut_function(almonds, pecans, cashews, walnuts):
	print "You have %d Almonds!  Eat em up!" % almonds
	print "And %d Pecans.  I love Pecans -- will you share?" % pecans
	print "Cashews!  Save 'em for Lyd!  She'll love %d Cashews." % cashews
	print "Walnuts rock!  You have %d of them.  Eat em up!" % walnuts

# 1. run it directly with numbers as arguments
print "First we will run this using numbers entered as arguments"
nut_function(10, 15, 20, 25)

# 2. define new variables and run it with those
print "Now we will run this using variables set to specific values."
raw_input()
my_faves = 12
lyd_faves = 22
seb_faves  = 20
kel_faves = 100

nut_function(my_faves, lyd_faves, seb_faves, kel_faves)

# 3. take input from the user and run it with those
print "Now we are going to make the function run with your inputs.  It's your world now!"
almonds = raw_input("How many almonds do you have? ")
pecans = raw_input("How many pecans do you have? ")
cashews = raw_input("And Cashews? ")
walnuts = raw_input("Give me them Walnuts! ")

nut_function(int(almonds), int(pecans), int(cashews), int(walnuts))

# 4. add variable bound values to integers
## $1 = 6 nuts
## if a person has 10 dollars, they can get 40 more nuts, spread out over all types
## so, take the dollars, multiply it by 4, and then
## distribute that number evenly over each type
## so, programatically, i'll need
## a. an input from the user -- check
## b. a conversion to number of nuts -- check
## c. a divider by 4
## d. input that divider into the function
print "Now I am going to convert the number of nuts you could have based on your money."

dollars = raw_input("How many dollars do you have? ")
converted = ((int(dollars) * 6) / 4) # convert the dollars to nuts

print "Great, that means we can increase the number of nuts you have by %d for each type." % converted

nut_function(int(almonds) * int(converted), int(pecans) * int(converted), int(cashews) * int(converted), \
int(walnuts)* int(converted))

# 5. multiply the raw_input taken above with integers



