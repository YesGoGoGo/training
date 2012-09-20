my_name = 'Brian R. Dant'
my_age = 30
my_height = 72 # inches
my_weight = 186 # lbs
my_eyes = 'Hazel'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eys and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, so try to get it exactly right
print "If I had %d, %d, and %d I get %d." (
    my_age, my_height, my_height, my_age + my_height + my_weight)
