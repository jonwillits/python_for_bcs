"""
What is the difference between a file name, a file handle, and file content?
COMMENT REQUIRED
"""

"""
In the code below, what is the difference between f.read() and f.readline(). What is a situation where you might want
to use each one?
COMMENT REQUIRED
"""
print('\n')
print("Example 0")
filename = 'test_file1.txt'
f = open(filename)
text = f.read()
print(text)
f.close()
print()


# your answer here
print()
print("Example 1")
filename = 'test_file1.txt'
f = open(filename)
line = f.readline()
print(line)
line = f.readline()
print(line)
line = f.readline()
print(line)
f.close()
print()


"""
In the code above, if you comment out line 24, f = open(filename), the code will now get an error. Why?
COMMENT REQUIRED
"""


"""
Rewrite the code from above so that it uses a for loop to iterate over each line in the file, convert each line to
all caps, and then print it out.
CODE REQUIRED, BUT DO IT ABOVE, REPLACING THE CODE FOR EXAMPLE 1
"""


"""
Examples 0 and 1 look slightly different when they print out. How and why are they different? If you are stumped, try
adding each line o a list, and then printing out the whole list at the same time. What do you notice about the lines
when they are in the list?
COMMENT REQUIRED 
"""

"""
The new line character \n is a hidden, invisible character that prints a return when it is encountered. You can remove 
it, or anything, by using the .strip() method for a string.
"""
print()
print("Example 4")
filename = 'test_file1.txt'
f = open(filename)
for line in f:
    text = line.strip('\n')
    print(text)
f.close()
print()

"""
Often you're dealing with a data file, like a comma-separated (csv) file, where you want to do stuff with different
columns of data separated by columns. you can use .split() to do this. split automatically gives you a list of items
separated by whatever character you tell it to use. Edit this code so that it prints only the animals, not their 
geographical location
CODE REQUIRED
"""
print("Example 5")
filename = 'test_file2.txt'
f = open(filename)
for line in f:
    data = line.strip('\n')
    data = data.split(',')
    print(data)
f.close()
print()

"""
You can split and strip based on any character or set of characters that you put in the function as an argument.
for example, line.split(' ') splits on spaces, line.split('.') splits on periods, and line.split('ri') will split on
any 'ri' that is encountered. Test each of these examples on 'test_file2.txt' below. Strip works the same way. But 
remember, strip only removes the specified characters from the beginning or end of a string, it won't remove them from
the middle. Experiment with stripping different characters and type in a comment block below how it works.
CODE REQUIRED
COMMENTS REQUIRED
"""

