# import the argv function from the sys module
from sys import argv

# define the variables that argv should look for from the command line in this particular case / for this file
script, first, second, third = argv

# ouput this text followed by the variables as defined by the argv statement above (as defined by the user who input them into argv from the command line)
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
