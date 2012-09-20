from sys import argv

script, input_file = argv

# define the function print_all, which will take the argument "f"
## this function will read the argument (or is it variable?) f and output it to the screen
def print_all(f):
	print f.read()

# define the function rewind, which will take the argument "f"
# this function will seek on "f", whatever the heck that means!	oh, that means that it will go to a certain place in the file; the 0 entered here indicates that it will start at the beginning of the file
def rewind(f):
	f.seek(0)

# define the function print_a_line, which will take the arguments one_count and "f"; note that this is the first time I am encountering the same argument being fed to multiple functions
#print_a_line will output the value bound to the variable line_count and also the output from f.readline(), whatever the heck that is!  oh, that's just a way of telling python to go to a certain file line and read what that line says, and nothing more!
def print_a_line(line_count, f):
	print line_count, f.readline()

# define the variable current_file which opens the input file, which is bound to that name by argv
current_file = open(input_file)

# output the text within the string
print "First let's print the whole file:\n"

# call the function print_all, which will read the argument, which is the input_file that has been opened by the open function through the current_file variable
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# run the function rewind
## this will run the function rewind, which will set the current location of the file; later when we run the function print_a_line, it contains the function (woah!  a function can contain a function!) readline which will read from the current position onward; that's why we first need to "rewind" the file with seek() to get it set to the location we want
rewind(current_file)

print "Let's print three lines:"

# bind the value 1 to the current_line name
## print_a_line will take the argument current_line and current_file; the function is defined to take its first argument and just print that line number, the second argument will read the output from the variable current_file and print whatever line has been put to current line. but how does readline know what line I want it to read?
current_line = 1
print_a_line(current_line, current_file)

# increase the value of current_line by 1 by changing the value that is bound to it
current_line += 1
# run the print_a_line function again
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_file.close()
