name = 'Georg'
age = 29 # not a lie
height = 179 # centimetres
weight = 71 # kg
eyes = 'Green-grey'
teeth = 'White'
hair = 'Brown'
hair_as_child = 'Blonde'

print "Let's talk about %s." % name
print "He's %d centimetres tall." % height
print "He's %d kilograms heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "When I was a child my hair was actually %s." % hair_as_child
print "When I was a child my hair was actually %r." % hair_as_child

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)