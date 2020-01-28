# describe in a comment what each commented line does
# comment out the lines that generate errors, but make sure you still describe why they dont work

number_list = []

object_list = ['dog', 'cat', 'shoe', 'sock']


print(number_list)
print(object_list)

print(object_list[0])
print(number_list[0])

number_list.append(5)
number_list.append(6)
print(number_list)

object_list.append('car')
print(object_list)

if 'shirt' in object_list:
    print('shirt is in the list')
else:
    print('no shirt in the list')

object_list[2] = 'shirt'
print(object_list)

if 'shirt' in object_list:
    print('shirt is in the list')
else:
    print('no shirt in the list')

num_items = len(object_list)
print("there are {} items in object list".format(num_items))

'''
    Questions:
    
    00. if i wanted to insert 'tree' into the 3rd position in the object list, so that it does NOT replace any items,
        how do I do that?
    01. what is the difference between list.pop() and list.remove()
    02. print out the object list, sorted in reverse alphabetical order

'''