from sys import exit 
from random import randint 


class Engine(object):

	def __init__(self, start):
		self.start = start

	def play(self):
		next = self.start 				#next equals a string that was sent in the object instantiation

		while True:
			print "\n--------"
			room = getattr(a_map, next) #this must just bring the attribute in for use from another class; then assigns the name of that
										#attribute to room (this must be different than just calling the function); the following line
										#actually calls the method (which you couldn't do unless you had already getattr()ed that attr)
			print "This is the line after the getattr()"
			next = room() 				#finally, this line actually runs the method and then assigns a name to next


class Map(object):
	
	def __init__(self):
		self.quips = [
			"You died.  You kinda suck at this.",
			"Nice job, you died ...jackass.",
			"Such a luser.",
			"I Have a small puppy that's better at this."
		]

	def death(self):
		print self.quips[randint(0, len(self.quips)-1)]
		exit(1)

	def central_corridor(self):
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew.  You are the last surviving member and your last"
		print "	mission is to get the neutron destruct bomb from the Weapons Armory,"
		print "	put it in the bridge, and blow the ship up after getting into an"
		print "	escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapons Aromory when"
		print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
		print "flowing around his hate filled body.  He's blocking the door to the"
		print "Armory and about to pull a weapon to blast you."
			
		action = raw_input(">")

		if action == "shoot!":
			print "Quick on the draw you yank out your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body, which throws"
			print "off your aim.  Your laser hits his costume but misses him entirely.  This"
			print "completely ruins his brand new costume his mother bought him, which"
			print "makes him fly into an insame rage and blast you reatedly in the face until"
			print "you are dead.  The he eats you."
			return 'death'
				
		elif action == "dodge!":
			print "Like a world class boxer you dodge weave, slip and slide right"
			print "as the Gothon's blaster cranks a laser past your head."
			print "In the middle of your artful dodge your foot slips and you"
			print "bang you head on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on"
			print "your head and eats you."
			return 'death'
			
		elif action == "tell a joke":
			print "Lucky for you they made you learn Gothon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhrf, fur fvgf nebhaq gur ubhfr."
			print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
			print "While he's laughing you run up and shoot him square in the head"
			print "putting him down, then jump through the Weapon Armory door."
			return 'laser_weapon_armory'
			
		elif action == "call your mom":
			print "Your mom was not the person to call in this situation.  She is in Minnesota and you"
			print "are trying to fight Gothons here!  Don't do that again.  Since you wanted to call"
			print "your mommy so bad, you must need a break.  We will send you to the Virgin Islands"
			return 'virgin_islands'

		else:
			print "DOS NOT COMPUTE!"
			return 'central_corridor'
			
	def laser_weapon_armory(self):
		print "You do a dive roll into the Weapon Armory, crouch and scan the room"
		print "for more Gothons that might be hiding.  It's dead quiet, too quiet."
		print "You stand up and run to the far side of the room and find the"
		print "neutron bomb in its container.  There's a keybpad lock on the box"
		print "and you need the code to get the bomb out.  If you get the code"
		print "wrong 10 times then the lock closes forever and you can't"
		print "get the bomb.  The code is 3 digits."
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[keypad]")
		guesses = 0
		cheat = 123

		while int(guess) != code and int(guess) != cheat and guesses < 9:
			print "BZZZZEDDD!"
			guesses += 1
			guess = raw_input("[keypad]> ")
			
		if int(guess) == code or int(guess) == cheat:
			print "The container clicks open and the seal breaks, letting gas out."
			print "You grab the neutron bomb and run as fast as you can to the"
			print "bridge where you must place it in the right spot."
			return 'the_bridge'
		else:
			print "The lock buzzes one last time and then you hear a sickening"
			print "melting sound as the mechanism is fused together."
			print "You decide to sit there, and finally the Gothons blow up the"
			print "ship from their ship and you die."
			return 'death'


	def the_bridge(self):
		print "You burst onto the Bridge with the neutron destruct bomb"
		print "under you arm and surprise 5 Gothons who are trying to"
		print "take control of the ship.  Each of them has an even uglier"
		print "clown costume that the last.  They haven't pulled their"
		print "weapons out yet, as they see the active bomb under your"
		print "arm and don't want to set it off."
		
		action = raw_input("> ")

		if action == "throw your bomb":
			print "In a panic you throw the bomb at the group of Gothons"
			print "and make a leap for the door.  Right as you drop it a"
			print "Gothon shoots you right in the back killing you."
			print "As you die you see another Gothon frantically try to disarm"
			print "the bomb.  You die knowing they will probably blow up when"
			print "it goes off."
			return 'death'
			 
		elif action == "slowly place the bomb":
			print "You point your blaster at the bomb under your arm"
			print "and the Gothons put their hands up and start to sweat."
			print "you inch backweard to the door, open it, and then carefully"
			print "place the bomb on the floor, pointing your blaster at it."
			print "you then just back through the door, punch the close button"
			print "and blast the lock so the Gothons can't get out."
			print "Now that the bomb is placed you run to the escape pod to"
			print "get off this tin can."
			return 'escape_pod'
		else:
			print "DOES NOT COMPUTE!"
			return "the_bridge"
			
	def escape_pod(self):
		print "You rush through the ship desperately trying to make it to"
		print "the escape pod before the whole ship explodes.  It seems like"
		print "hardly any Gothons are on the ship, so your run is clear of"
		print "interference.  You get to the chamber with the escape pods, and"
		print "now need to pick one to take.  Some of them could be damaged"
		print "but you don't have time to look.  There's 5 pods, which one"
		print "do you take?"

		good_pod = randint(1,5)
		guess = raw_input("[pod #]> ")

		
		if int(guess) != good_pod:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod escapes out into the void of space, then"
			print "implodes as the hull ruptures, crushing you body"
			print "into jam jelly."
			return 'death'
		else:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod easily slides out into space heading to"
			print "the planet below.  As it flies to the planet, you look"
			print "back and see your ship implode then explode like a"
			print "bright star, taking out the Gothon ship at the same"
			print "time.  You won!"
			exit(0)

	def virgin_islands(self):
		print "You made it to the Virgin Islands!  You are one lucky bastard.  Now you will get to"
		print "decide how many Margaritas you will drink with the Lula Women."

		drinks = raw_input("> ")
		
		if int(drinks) > 0 and int(drinks) <= 3:
			print "Ok, you only had a few drinks, that wasn't too bad.  You should be able to"
			print "fight the Gothons just fine Get back out there and start over!"
			return 'central_corridor'

		elif int(drinks) > 3 and int(drinks) <=6:
			print "You aren't wasted, but you're going to have some trouble.  As a matter of fact, some"
			print "dude is claiming that you were macking on his wife!  He happens to be a captain"
			print "of your force with the power to ship you to the middle of a battle!  Good luck!"
			return 'the_bridge'

		elif int(drinks) > 6:
			print "That was a mistake!  You are wasted.  Sorry, but you can't go on!"
			return 'death'

a_map = Map()
x_engine = Engine("central_corridor")
x_engine.play()
