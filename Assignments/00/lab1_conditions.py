"""
Here we are just defining some variables that we are going to use below.
"""

X = 1
Y = 2
Z = 10

A = '0'
B = '1'
C = '10'
D = 'dog'

"""
One common kind of statement in a computer program is one that contains a 'conditional' comparison between two things. A
simple conditional typically has four parts:
    - the word 'if'
    - two things being compared
    - an 'operator' that specifies the kind of comparison being made

In this first example, we are just comparing two numbers, and executing the code underneath and tabbed to the right
depending on whether the expression in the if statement evaluates to be True or False. In this case, the operator is 
>, and so whether the 'if' condition true or false should be pretty obvious.
"""

if 5 > 3:
    print("5 is greater than 3")
else:
    print("5 is not greater than 3")


"""
A more common way to do an if statement is using variables you want to compare, which might be changing in the course of
your program so that, unlike in the example above, its not obvious whether the if condition will be true or false. 
Without modification, X contains the string '0', and D contains the string 'dog', and the double equals operator is the 
way to test whether they are exactly the same. In this case they are not, and so the 'if' condition will be false, and 
the code in the 'else' condition will run. 

Modify the code below by adding a statement on line 42 that changes the value of X or D such that the 'if' condition
will evaluate to True, and "Same" will be printed. 
"""

""" CODE REQUIRED """
if X == D:
    print("Same")
else:
    print("Different")


"""
We can of course print variables or run any code we want in the if and else conditions,
"""
if X > Y:
    print(X)
else:
    print(Y)

"""
For each of the following comparisons below, add to the comment stating whether the if will evaluate to True or False,
and explain why.

COMMENT REQUIRED
    Y & Z
    X & Z
    A & B
    A & C
    B & C
    C & D
    Z & C 
"""

""" 
What will this 'AND' code do? 
COMMENT REQUIRED
"""
if (X > Z) and (int(A) == X):
    print("Success")
else:
    print("Fail")

""" 
What about this 'OR' code? 
COMMENT REQUIRED
"""
if (X > Z) or (int(A) == X):
    print("Success")
else:
    print("Fail")

""" 
Is this logically equivalent to the AND code or to the OR code
COMMENT REQUIRED
"""
if X > Z:
    if int(A) == X:
        print("Success")
    else:
        print("Fail")
else:
    print("Fail")

""" 
How would you modify the code above to make it logically equivalent to the whichever one (AND/OR) that it was not like?
In other words, if the code above is like the AND code, change it to behave like the OR code, but continuing to use two 
separate if statements instead of one combined one
CODE REQUIRED
"""