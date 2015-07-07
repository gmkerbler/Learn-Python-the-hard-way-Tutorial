from sys import argv

script, filename = argv

readfile = open(filename, 'r')

print "Reading .. %r .." % filename
readfile.read()

print "Now we're printing this file"
print readfile

readfile.close()