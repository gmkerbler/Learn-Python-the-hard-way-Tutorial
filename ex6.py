x = "There are %d types of people." % 10 	#set x as string ".." with formatter defined as 10
binary = "binary"							#set variable binary as string "binary"
do_not = "don't"							#set variable do_not as string "don't"
y = "Those who know %s and those who %s." % (binary, do_not)	#set variable y as string including two formatters, defined as binary and do_not

print x		#print string x - see line 1
print y		#print string y - see line 4

print "I said: %r." % x				#print the string "I said:" with formatter %r (prints everything) as variable/string x - converts double quotes into single quotes
print "I also said: '%s'." % y		#print string "I also said: .." with formatter %s including single quotation marks '%s' - formatter is variable y

hilarious = False			#set variable "hilarious" as boolean expression "False" - can be set as "True" as well
joke_evaluation = "Isn't that joke so funny?! %r"  #set var joke_ev.. as string with formatter %r - don't have to define formatter right after, can just later on call variable and define formatter as you want

print  joke_evaluation % hilarious		#print the var joke_ev.. set formatter to true - still just prints true, even though it's a boolean values and not a string

hilarious = True
print "Isn't that joke not so funny?! %r" % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
print w+e
print w   +   e