#import from module sys the variale argv (user-prompted input when opening file)
from sys import argv
#variables script and filename are stored to argv 
script, filename = argv
#variable txt is set as opening the 2nd argv variable (a text-file) and gives the variable "txt" the opssibility to give it commands
txt = open(filename)
#a message is printed displaying also the filename (argv variable), called upon with a formatter
print "Here's your file %r:" % filename
#Now we're printing the variable "txt" which is our text file by putting a dot "." and the command read, as ".read" behind the file
#the command is executed without setting any parameters, hence the empty brackets
print txt.read()
#here the user is prompted to give a raw_input, again the name of the text file we just printed and it assigned to variable "> "
#and saved to the variable txt_again
print "Type the filename again:"
file_again = raw_input("> ")
#now the variable txt_again is given command-able powers by assigning it the "open" ability re: our text-file
txt_again = open(file_again)
#again we execute a command on the text file by using the "open" function through the dot "." at the end of the before assigned variable
#and print its content (without any parameters)
print txt_again.read()