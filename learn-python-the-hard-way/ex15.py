# import the argv function from the sys library / module
from sys import argv

# define what the command line arguments passed to argv will do / be
script, filename = argv

# bind the right side of this to the name "txt"; the right side is a function that will open the file associated with "filename"
# OR you could say the value bound to txt is the contents of the file
## note that the file that will be opened is the one defined by the second argument passed to the interpreter from the command line
txt = open(filename)

## this will print the name of the second argunment send from the command line
print "Here's your file %r:" % filename

# (?) get the value bound to the name "txt" and read it (?); but does the .read() part need to come after something has been opened? yes; i tried "print filename.read()" and got an attribute error
print txt.read()

print "I'll also ask you to type it again:"

# assign the value from the user prompt to the name "file_again"

file_again = raw_input("> ")

# bind the function "open", which is being fed the argunment file_again, to the name "txt_again"
txt_again = open(file_again)

# read the value bound to txt_again and output it
# note again that the read function (?) can only be used when the name / variable it is reading is bound to a function that opens the file
print txt_again.read()

txt.close()
txt_again.close()
