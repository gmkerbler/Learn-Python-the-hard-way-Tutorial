print "ASCII backspace, deletes a single space before it"
print "** blabla \b blabla" #\b is an ASCII backspace, which deletes a single space before it

print "ASCII bell, puts a single space before it"
print "** blabla \a blabla" #\a is an ASCII bell, which puts a single space before it

print "ASCII formfeed, puts a new line and a tab after it"
print "** blabla \f blabla"

print "ASCII linefeed, puts a new line after it"
print "** blabla \n blabla"

print "ASCII %r tab, puts a new line and tab after it" % "vertical"
print "** blabla \v blabla"

print "ASCII %s tab, puts a tab without new line after it" % "horizontal"
print "** blabla \t blabla"

print "Carriage %r" % 'return'
print "** blabla \r blabla"

print "If i want to print a backslash i just write two like this: 6 \\ 3 = 2"
