print "You enter a dark room with two doors.  Do you go through door #1, #2, or #3?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating cheese cake.  What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your face off.  Good job!"
	elif bear == "2":
		print "The bear eats your legs off.  Good job!"
	else:
		print "Well, doing %s is probably better.  Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello.  Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck.  Good job!"

elif door == "3":
	print "You walk into Pebble Beach.  Who would you like to play with?"
	print "1. Stevie -- Tiger's old caddie."
	print "2. Tom Watson (is it really a question?)"
	print "3. Old Tom Morris -- you can talk about winning the same major 6 times."
	print "4. Tiger Woods -- you can ask for marital advice."

	fav_player = raw_input("Who's it gonna be?" )

	if fav_player == "1":
		print "You and Stevie play 18 holes, have a Vodka Tonic overlooking the ocean."
	elif fav_player == "2":
		print "Tom and you play the front 9, and then you go to the range for a lesson."
	elif fav_player == "3":
		print "That's not possible -- he's dead."
	elif fav_player == "4":
		print "You and Tiger went toe to toe until he hooked it in the water on 18."
	elif fav_player == "Secret Door":
		print "Now you're talking!  Let's play the real game."
		print "What course do you really want to play?"

		the_real_deal = raw_input("Tough Choices!" )

		if the_real_deal != "BD's Home Turf":
			print "Man you know I love %s!  Can I come with?" % the_real_deal

		else:
			print "Ok now you are in for it!  Let's take it to the 'Tine!"
			print "You vs. BD!  What hole do you want to start on?"
			print "1, 10, or 6?"

			hole = raw_input("> ")

			if hole == "1":
				print "You both hit it down the middle, and BD stuffed a 7 iron to six feet."
				print "You've got 155 with a head-wind coming slightly from the left."
				print "What club will you hit?"

				club = raw_input("> ")

				if club == "8":
					print "Oh man!  You should have taken on more.  It plugged in the bunker :-("
				elif club == "7":
					print "Yes!  Great choice!  You stiffed it!  Now you just have to putt vs. the master!"
				else:
					print "What the hell is that?  That won't work!"

			else:
				print "You can't do that, the starter busted you!"
	else:
		print "Don't you like those guys?"
else:
	print "You stumble around and fall on a knife and die.  Good job!"
