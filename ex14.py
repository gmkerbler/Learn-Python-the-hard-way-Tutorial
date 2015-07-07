from sys import argv

script, user_name, user_geneticmakeup = argv
prompt = '< '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few question."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "Your %s is interesting, can I ask how old you are?" % user_geneticmakeup
age = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
Also your %r correlates with your %r. Cool.
""" % (likes, lives, computer, user_geneticmakeup, age)