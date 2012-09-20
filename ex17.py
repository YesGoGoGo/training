from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
# open the from_file and bind it to input
##
###
input = open(from_file)
indata = input.read()
# read the file opened by input and bind that read content to "indata"

# find the length of the file
print "The input file is %d bytes long" % len(indata) # note that this is done after the file is 1) assigned to a variable 2) opened by another variable / assignment statement 3) read by a third variable

# use the exist method to check if the to_file exists
###
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to contunue, CTRL-C to abort." # not that whenever you prompt someone, they have the option to ctrl-c to end it, or hit enter to continue it
raw_input()

## in the followign statemtne, we are going to write the data, that has been taken out of the from_file, and put it into the to_file.  The from_file needed to be 1) attached to a variable name through argv, 2) then opened with the open function and that was assigned to a variable, and then 3) read with another method and assigned to a third variable, and below we will 4) take the data and write it to the new file with the write method
# open the to_file with write capabilities
output = open(to_file, 'w')
# write the contents of the from_file, which is bound to "indata" to the output variable which is bound to the file from_file
output.write(indata)

print "Alright, all done."

# close both files
output.close()
input.close()
