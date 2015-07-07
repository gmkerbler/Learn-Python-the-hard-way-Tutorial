def calculator(first, second, third):
    print "I'm a calculator"
    print "I will perform the following equation: a + b + c"
    print "a is %r, b is %r, c is %r" % (first, second, third)
    print "%r + %r + %r = %r" % (first, second, third, (int(first) + int(second) + int(third)))
    
calculator(1, 2, 3)

first = 9
second = 7
third = 4

calculator(first, second, third)

calculator(first ** 2, second ** 2, third ** 2)

print "Or just give me three numbers:"
first = int(raw_input())
second = int(raw_input())
third = int(raw_input())

calculator(first, second, third) 