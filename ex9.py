# Here's some new strange stuff, remember type it exactly

days = "Mon Tue Wed Thu Fri Sat Sun"				#set variable "days" as string "Mon Tue ..."
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"	#set variable "months" as string "Jan\nFeb ..." where \n sets a new line wherever its used

print "Here are the days:", days					#print the expression "Here are ..." followed by the variable "days", separated by a comma	
print "Here are the months:", months				#print the expression "Here are .." followed by the variable "months", separated by a comma

#print the following expression, set up with three quotation marks, meaning it can span as many lines as you want - you also can not comment using the hash next to these lines as it will be taken as part of the string
print """											
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

print "blablabla %r blabla" % ("\nJan\nFeb\nMar") #when using the formatter %r it will give the raw "data" and not react to the new line term "\n"