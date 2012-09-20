from sys import argv

# goal: use raw_input and argv to get more input from the user

# bind the value that the users gives to this question to the name "funny_fact" which will be stored in the global namespace
funny_fact = raw_input("What's the funnist thing you know? ")

# bind the value given by the user through the raw input function to the name "longest_belch"
longest_belch = raw_input("What's the longest belch of your life? ")
best_story = raw_input("What's the best story you have ever heard? ")

# define how the inputs from the command line will be bound into argv 
script = argv

# output the text (string) inside the quotes and fill the format characters with the variable names listed after the modulo 
print "The name of the script is: %r" % script
print "You're funny fact is %s, and that's pretty funny!" % funny_fact
print "That is a really long belch, did you really belch for %s?" % longest_belch
print "That is a terrible story, you really need to get it together with your story telling!  Do you really think someone wants to hear about %s?" % best_story


