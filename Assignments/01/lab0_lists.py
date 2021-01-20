"""
Starting this week, the labs will tend to do less of the explaining, and just ask you to do stuff. If you aren't sure
how to answer the questions asked below, check back to the week's assigned readings.

In this file:
- everywhere you see a "COMMENT REQUIRED", add a comment explaining what the next lines do
- comment out any lines that generate errors, and explain in a comment why they don't work
- answer the three questions at the bottom of the file
"""


# COMMENT REQUIRED
number_list = []

# COMMENT REQUIRED
object_list = ['dog', 'cat', 'shoe', 'sock']

# COMMENT REQUIRED
print(number_list)
print(object_list)
print(object_list[0])
print(number_list[0])

# COMMENT REQUIRED
number_list.append(5)
number_list.append(6)

print(number_list)

object_list.append('car')
print(object_list)

# COMMENT REQUIRED
if 'shirt' in object_list:
    print('shirt is in the list')
else:
    print('no shirt in the list')

# COMMENT REQUIRED
object_list[2] = 'shirt'
print(object_list)

# COMMENT REQUIRED
if 'shirt' in object_list:
    print('shirt is in the list')
else:
    print('no shirt in the list')

# COMMENT REQUIRED
num_items = len(object_list)
print("there are {} items in object list".format(num_items))

"""
If i wanted to insert 'tree' into the 3rd position in the object list, so that it does NOT replace any items, how do 
I do that?
CODE REQUIRED
"""
    
"""
What is the difference between list.pop() and list.remove()
COMMENT REQUIRED
"""

"""
Print out the object list, sorted in reverse alphabetical order
CODE REQUIRED
"""

