#creates a function using the "def" command (define) - after def we specify function name and in brackets the inputvariables
#after the variables we write a colon, indicating what the function will actually do
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party."
    print "Get a blanket.\n"
#As you can see after the colon every line is indented by 4 spaces, which makes it part of the function, in our case really
#just a series of simple print-commands, using our previously defined variables through formatters as part of the print
    
#now we call the function, by typing its name, and, then in brackets we set however many variables we need to whatever we want, in our
#case we simply give it two numbers, by calling the function it is automatically executed, so everything we defined above is printed
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#Alternatively to just calling the function rightaway we can also set the variables as numbers and then simply run the function after,
#this time using the variables instead of just raw numbers
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Also, we (as the print text says) can feed some maths into the function, where it will use the result of the operation as input
#make sure you always separate arguments by commas
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#Then we simply combine all of the three variations above to specify the function input
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)