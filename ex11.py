print "How old are you?", #prints the string, then asks for input - can be anything, numbers, letters or combination
age = raw_input()
print "How tall are you?",	#prints the string, then asks for input - can be anything, numbers, letters or combination
height = raw_input()
print "How much do you weigh?",	#prints the string, then asks for input - can be anything, numbers, letters or combination
weight = raw_input()
print "what is this?"
explanation = raw_input() #by the way, every input to raw_input() will be treated as a string
#you could also write: explanation = raw_input ( " What is this: " )
explanation = raw_input ( " What is this: " )

print "So, you're %r old, %r tall and %r heavy." % ( #prints the string, taking all variables that were set by the user before into one print sentence, like an endresult
	age, height, weight)
	
print "This looks neater: So, you're %s old, %s tall and %s heavy." % ( #looks nicer to use %s so you don't see all the single quotation marks
age, height, weight)

print "That is your explanation to what is going on here: %s" % explanation

print "How many legs do you have?"
number_of_legs = int(raw_input())
print number_of_legs