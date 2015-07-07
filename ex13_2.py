from sys import argv

script, a, b = argv

print "This script's name is", script
print "number 1", a
print "number 2", b

x = int(raw_input ( "First number times:"))

i = int(raw_input ( "Second number times:"))

j = (int(a) * x)
jj = (int(b) * i)

print j
print jj