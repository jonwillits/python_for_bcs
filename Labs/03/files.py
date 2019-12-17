'''
    what is the difference between a filename, a file handle, and file content?
'''
print('\n')
print("Example 01")
filename = 'test_file1.txt'
f = open(filename)
text = f.read()
print(text)
f.close()
print()

'''
    what is the difference between f.read() and f.readline()
'''
# your answer here
print()
print("Example 02")
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

'''
    so the above is nice because you can do a line at a time. but you need type it once for each line. that's annoying.
    use a for loop to iterate over a file
    note that the syntax here is a lot like the syntax for iterating over a list.
    the for loop automatically lets us create a variable that gives us the lines from the file, one at a time.
'''
print()
print("Example 03")
filename = 'test_file1.txt'
f = open(filename)
for line in f:
    print(line)
f.close()
print()

'''
    Examples 02 and 03 both print out slightly differently from Example 01.
    This is because of hidden "new line characters
    To see what this means, try adding each line to a list, and then printing the list
'''
# how are 02 & 03 different from 01?

print("Example 04")
filename = 'test_file1.txt'
line_list = []
f = open(filename)
for line in f:
    line_list.append(line)
f.close()
print(line_list)
print()

'''
    the new line character \n is a hidden, invisible character that prints a return when it is encountered.
    You can remove it, or anything, but using .strip()
'''
print()
print("Example 05")
filename = 'test_file1.txt'
f = open(filename)
for line in f:
    text = line.strip('\n')
    print(text)
f.close()
print()

'''
    often you're dealing with a data file, like a comma-separated (csv) file, where you want to do stuff with different
    columns of data separated by columns. you can use .split() to do this. split automatically gives you a list of items
    separated by whatever character you tell it to use. 
    Edit this code so that it prints only the animals, not their geographical location

'''
print("Example 06")
filename = 'test_file2.txt'
f = open(filename)
for line in f:
    data = line.strip('\n')
    data = data.split(',')
    print(data)
f.close()
print()

'''
you can split and strip based on any character or set of characters that you put in the function as an argument.
for example, line.split(' ') splits on spaces, line.split('.') splits on periods, and line.split('ri') will split on
an 'ri' that is encountered. test each of these examples on 'test_file2.txt' below. Strip works the same way.
Experiment with stripping different characters and type in a comment block below how it works.
'''
# your code here
