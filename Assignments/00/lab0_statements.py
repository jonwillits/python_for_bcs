"""
This is a python file, which you can tell by the fact that the file name ends in '.py'. Python files consist of code
and comments. Comments, like what you are reading now, are text that is ignored by the python program interpreter.
The python interpreter knows this is a comment because it is separated by three double quotes at both the beginning and
end of the comment.

In this and in all future labs, there will be a mix of instructional material you read, code you run, and occasionally
a place where you are required to either modify the code or add a comment. In these situations, there will be an
explicit prompt that either says CODE REQUIRED or COMMENT REQUIRED that lets you know you need to change this file in
some way to get full points for the lab. Before you turn in a lab file, it would be a good idea to do a search through
each file for the word REQUIRED, to make sure you've answered them all.
"""

'''
You can also create python comments with three double quotes, instead of single quotes. There are a number of reasons
why python uses both. One is so that you can include quotes in your comment. Within this comment denoted by single 
quotes, I can use three double quotes, """, and it doesnt result in the end of the comment. In most situations, you can 
use either single or double-quotes depending on your preference, and based on whether you want to include single or 
double quotes inside the quotes.
'''

# The third way, and most common way, to denote comments is using # at the beginning of the line.
# Notice that for the quoted comments above, each line doesnt have to start with a quote, you can just type whole
# paragraphs. But with #, you must have a # at the beginning of each line. So if you are writing a short comment,
# most people use a #, but if you need to write a whole paragraph, most people use triple quotes.

"""
Anything without a # or quote will be treated by the python interpreter as code. Each line of python code is called a 
statement. One kind of statement is assigning values to variables. In this first lab, we are introducing three of the 
most basic types of variables: 

    1) string (text)
    2) int (whole number integers)
    3) float (floating point numbers, or decimals)

In python, unlike many programming languages, you dont need to tell python what kind of data is stored in a variable. 
Python is called an 'interpreted' language, because it figures this out on its own. Python knows that the data being 
assigned to a variable is a string if it is enclosed in single or double quotes, like a through d below. Just like with 
comments, you can use single or double quotes, and part of the reason for this is so that your string can include quotes 
(of whatever type you did not use to surround the string).
"""

a = 'dog'
b = 'pizza'
c = "shoe"
d = "isn't"

"""
If a value has quotes, python interprets it as a string. This is true even if it is a number. Below, 'w' is a string, 
even though it has 5 as its value. If a value doesnt have quotes, python will interpret it as a int if it is a number 
without a decimal, and as a float if it is a number with a decimal.
"""

x = '5'
y = 30
z = 4.0

"""
A final case we will consider is variable 'm', where we are assigning one variable to another. The result of this line
is that 'm' will have the value we have previously stored in 'a', dog. If you mean to assign a string but forget the 
quotes, python will think you are trying to assign one variable to another. Below, 'n' is being assigned the value
of whatever is stored in a variable called pizza, but because that variable doesn't exist (we never created it), this
line would generate an error if it weren't commented out.
"""

m = a
# n = pizza

"""
Beyond assigning values to variables, another common type of python statement is an 'expression', where variables are
being combined in some way according to the rule specified by the 'operator'. A common example is addition of numbers.
We can add our variables x and y, which both contained numbers. Note that y was an int, and z was a float. When they 
are added, python automatically makes the result a float as well, retaining the extra information that had been
contained in z.
"""

the_sum = y + z

"""
Another kind of statement is a print() statement, which we can use to view the values stored in variable.
print statements can have single variables or multiple variables separated by commas.
"""

print(y)
print(z)
print(the_sum)
print(y, z, the_sum)  # example of print statement with multiple variables.

"""
Below are some statements using different operators combined with our variables. What is the output of the following 
statements? Uncomment each one and see if and how it works. For each line create a comment to the right of each
statement that explains what is happening, and if it generates an error, why that error occurs.

COMMENTS REQUIRED
"""
# print(x + y)
# print(a + b)
# print(a + m)
# print(y += 5
# print(y - z)
# print(a - b)
# print(y * z)
# print(y ** z)
# print(a * 5)
# print(a * b)
# print(a / b)
# print(y / z)
# print(y // z)
# print(y % z)


# if you wanted to print out A and X, resulting in "DOG 30", how would you do that?
"""
CODE REQUIRED
"""