"""
dictionaries are like lists, except that:
  - instead of a ORDERED sequence that you can access by it's number,
  - the information is stored as unordered KEY-VALUE pairs
  in the example below, the cities are the KEYS, and the populations are the VALUES

you define dictionaries with squiggly brackets
"""
north_america_city_populations_dict = {
    "Mexico City": 8918653,
    "New York City": 8550405,
    "Los Angeles": 3971883,
}

"""
This is really nice. If we wanted to keep track of cities and their populations together (or any other pair of data
a label), we would need two lists like we did in last week's lab where we counted the word frequencies. 
"""
city_name_list = ["Mexico City", "New York City", "Los Angeles"]
city_population_list = [8918653, 8550405, 3971883]

"""
or a list of lists.
"""
north_america_city_populations_list = [["Mexico City", 8918653], ["New York City", 8550405], ["Los Angeles", 3971883]]


""" 
Imagine we wanted to look up New York's population. First we would have to find it in the list, and then access the
population. This is some extra code, but more importantly, could slow our program down if the list is long.
"""
for i in range(len(north_america_city_populations_list)):
    if north_america_city_populations_list[i][0] == 'New York City':
        population = north_america_city_populations_list[i][1]
        print(population)

"""
but with a dictionary, we can just do it in a simple lookup line
"""
population = north_america_city_populations_dict['New York City']
print(population)

"""
Behind the scenes, python is actually still doing a search for the key and returning you the value, but all that code is
hidden so your program looks nicer, and the search is also being implemented in a optimal way to reduce the search time.
"""

"""
Dictionaries are defined using {} instead of []. But notice when you look up a key in a dictionary, you still use square 
brackets just like a list or tuple. But instead of using a number to reference a spot in the list or tuple, you can just 
access the thing you are looking for by name.
"""


"""
What happens if you try to retrieve an item that is not in the dictionary?
What happens if you try to access a dictionary item using it's order, a number, like you do with a list
COMMENT REQUIRED
"""

"""
Just like a list, you can start with an empty list, dict = {}, and add things one at a time. Add a new entry to the 
dictionary defined above.
CODE REQUIRED
"""


"""
Below are some operators for dictionaries (or things you can do to them, as in + is an operator for an integer, a thing 
you can do to it). For each one, print them out so they make sense to you, then adda comment explaining what each does.
"""

# COMMENT REQUIRED
num_cities = len(north_america_city_populations_dict)

# COMMENT REQUIRED
del north_america_city_populations_dict['Los Angeles']

# COMMENT REQUIRED
if 'Los Angeles' in north_america_city_populations_dict:
    print(True)
else:
    print(False)


"""
Write and call a function that takes week 2's "test_file2.txt" as an input, (the file with the animals and where they 
are from), and put's each animal into the dictionary as a key, with the location as it's value. have the function
return the dictionary. Outside the function, write a loop that that iterates through the whole dictionary, printing them
out one at a time.

CODE REQUIRED
"""
