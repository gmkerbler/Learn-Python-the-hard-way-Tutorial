tabby_cat = "\tI'm tabbed in."			#setting variable "tabby_cat as string with a tab-command at the start
persian_cat = "I'm split\non a line."	#setting variable "persian_cat" as string with new line expression in it
backslash_cat = "I'm \\ a \\ cat."		#setting variable "backslash_cat" as string with double backslashes in it - don't know what that'll do - it'll print only one backslash instead of double

#setting variable "fat_cat" as string using triple double-quotation marks that includes a tab-command "\t" at every start of each line
#also includes stars and new line commands - will stars do anything? No, are just characters
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" % i,