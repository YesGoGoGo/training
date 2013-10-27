tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# playing with extra credit
print "-----"
print "\v\t\r-----\v\t\rjoemama\v\tfairytales\v\tbrian dant"
print "-----"

print "\b"

header = "-----"
stairs = "\t\v^" * 10
footer = "HI"

print "%s%s%s" % (header, stairs, footer)
