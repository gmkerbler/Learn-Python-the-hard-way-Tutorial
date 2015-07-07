from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input ( "?" )

print "Opening the file %r ..." % filename
target = open(filename, 'w')

print "Truncating the file"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")
line4 = raw_input("line 4:")

print "I'm going to write these to the file."
#target.write(" %r \\n %r \\n %r") % (line1, line2, line3)

target.write(line1) 
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.write(line4)

print "Now the file %r will be closed " % filename

target.close()