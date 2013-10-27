# import the argv function from the sys module
from sys import argv
# tell argv that these are the names to associate the command line inputs to
script, filename = argv

# output this text and fill the format character with the value bound to the name "filename"
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# prompt the user for an answer to the question printed above; note that this prompt does not get associated with anything but it could if it was preceded by <name> = ; it also shows that you can prompt the user to advance or stop just by using raw_input (although there isn't really input)
raw_input("?")

print "Opening the file..."

# bind the function open, which takes the parameters filename and "w"
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
# use the truncate funcation to clear the contents of the target
## the target is a variable that has bound to it the open function, which has been fed the filename argument, which itself is the file that was bound to that name by the argv tool(?), which was imported from the sys module  (and one other "w" that I don't really know what it does)
## "target" >> filename >> argv >> command line
target.truncate()

print "Now I'm going to ask you for three lines."

# bind the users input to the name line1
line1 = raw_input("line 1: ")

# bind the users input to the name line2
line2 = raw_input("line 2: ")

#bind the users input to the name line3
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# bind the values that the user inputted to the name / variable target
## since target is bound to a value that is a variable that is bound to a file, you can call the target variable in a write function and it will write to that file
target.write(line1)

# start a newline in the file
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."

## there need to be three layers of assignments here because:
## 1. you need a variable name to assign command line argunments to
## 2. you need a variable to put into the open function (since you can't just open a file and output it -- you need to open, and then read it)
## 3. you need a variable that you can send other instructions / functions (but the file need to be opened by the open function first before it can accept these other functions)
target.close()
