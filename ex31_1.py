print "Welcome, friend. How do you feel today on a scale of 1-3?"

x = raw_input("> ")
	
if x ==  "1":
	print "Oh no, I don't feel so great either, we should go do something fun!"
	print "Maybe you want to put on a costume:"
	print "1. Ladybug"
	print "2. Sloth"
	print "3. Unicorn"
	
	costume = raw_input("> ")
	
	if costume == "1":
		print "Oh, soo cuute!."
		print "Gotta go now, bye, see ya soon."
	
	elif costume == "2":
		print "Oh, soo lazyy."
		print "Gotta go now, bye, see ya soon."
		
	else:
		print "Oh, soo preetty."
		print "Gotta go now, bye, see ya soon."
	
elif x == "2":
	print "All average, huh? How 'bout some programming fun?"
	print "1. Yes"
	print "2. No"
	
	programming = raw_input("> ")
	
	if programming == "1" or pogramming == "2":
		print "Anyways, I have to put some pants on, can you decide me which ones?"
		print "1. The one with pictures of planets and stars?"
		print "2. The one with tiger stripes?"
		
	pants = raw_input("> ")
	
	if pants == "1":
		print "You little geek, you like stuff about the universe, huh?"
		print "Gotta go now, bye, see ya soon."
		
	elif pants == "2":
		print "Roooooaaaarrrr."
		print "Gotta go now, bye, see ya soon."
		
	else:
		print "No pants party or what?"
		print "Gotta go now, bye, see ya soon."
		
else:
	print "All swell. Want some cake?"
	print "1. Yes"
	print "2. No"
	
	cake = raw_input("> ")
	
	if cake == "1":
		print "Nothing better than some good old Linzertorte!"
		print "Gotta go now, bye, see ya soon."
		
	else:
		print "Wrong answer. This computer will destroy itself in 10 seconds. RUN!"
		print "Gotta go now, bye, see ya soon."