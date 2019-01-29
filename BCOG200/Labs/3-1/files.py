'''
    what is the difference between a filename, a file handle, and file content?
'''
print()
print("Example 1")
filename = 'test_file0.txt'
f = open(filename)
text = f.read()
print(text)
f.close()
print()

'''
    what is the difference between f.read() and f.readline()
'''
print()
print("Example 2")
filename = 'test_file0.txt'
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
print("Example 3")
filename = 'test_file0.txt'
f = open(filename)
for line in f:
    print(line)
f.close()
print()

'''Examples 2 and 3 both print out slightly differently from Example 1.'''
'''This is because of hidden "new '''
