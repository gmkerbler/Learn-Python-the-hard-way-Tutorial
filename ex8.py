formatter = "%r %r %r %r" #defined variable "formatter" as a string including 4 formatters that are not set to anything, kind of like placeholders

print formatter % (1, 2, 3, 4) #setting all the formatters to the number sequence "1 2 3 4"
print formatter % ("one", "two", "three", "four") #set the formatters to the strings "one two three four"
print formatter % (True, False, False, True) #set the formatters to the boolean values "True False False True"
print formatter % (formatter, formatter, formatter, formatter) #set formatters as the variable formatter which is defined as string in line 1
print formatter % (							#set the formatters as strings, which are expressions separated by a comma to output them all in the same line, but using good python style
		"I had this thing.",
		"That you could type up right.", 
		"But it didn't sing.",
		"So I said goodnight."
)	#have to close bracket again		

formatter = "%r %r %r %r" % ('eins', 'zwei', 'drei', 'vier')
print formatter