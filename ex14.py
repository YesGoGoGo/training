## this program uses argv to store / bind a users name and the script name to the variables "script and user_name"; then it takes those variables and puts them into questions about things in their life; from there, the user's responses are outputted into a comprehensive statemetn about their likes, etc

# import the argv funciton from the sys module
from sys import argv

# define what arguments argv will take
script, user_name, house_color = argv

# bind the string to the name prompt through an assignment statement
prompt = 'Write it here: '

# print this text and use the format character tool(?) to put the values of the variables into the string; in the order that they are listed here
print "Hi %s, I'm the %s script, and I'd like to ask you a few questions while you are sitting in your %s colored house." % (user_name, script, house_color)

# output / print this text string
print "I'd like to ask you a few questions."

# output / print this string and insert the value currently bound to the user_name variable / name where the format character is loacated within the string
print "Do you like me %s?" % user_name

# prompt the user, through the built-in function raw_input; the users response will then be the value bound to the name "likes"
likes = raw_input(prompt)

print "Where do you live %s?" % user_name

# prompt the user and bind their response to the name / variable "lives"
lives = raw_input(prompt)

print "What kind of computer do you have?"

# prompt the user and bind their response to the name computer
computer = raw_input(prompt)

# output whatever I type next exactly as I type it, ignoring the conventions normally associated with strings
# use the values bound to the likes, lives, and computer variable / name and insert them into this statement where the format characters are located, in the order they are listed
print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
