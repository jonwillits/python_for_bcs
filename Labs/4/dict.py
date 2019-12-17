# dictionaries are like lists, except that:
#   - instead of a ORDERED sequence that you can access by it's number,
#   - the information is stored as unordered KEY-VALUE pairs
#   in the example below, the cities are the KEYS, and the populations are the VALUES

# you define dicionaries with squiggly brackets
na_city_populations_dict = {
    "Mexico City": 8918653,
    "New York City": 8550405,
    "Los Angeles": 3971883,
}

# this is really nice. if we wanted to keep track of cities and their populations (or any other pair of data
#   a label, we would need two lists. or a list of lists.
na_city_populations_list = [["Mexico City", 8918653], ["New York City", 8550405], ["Los Angeles", 3971883]]


# to access a city's population from a list, we would need to know what spot it is in:
for i in range(len(na_city_populations_list)):
    if na_city_populations_list[i][0] == 'New York City':
        population = na_city_populations_list[i][1]
        print(population)

# but with a dictionary, we can just do it in a simple lookup line:
population = na_city_populations_dict['New York City']
print(population)
# notice that you use square brackets, like a list. this can be confusing. You definite dicts with {}, but access
# them with []

# under the surface, python is doing a search like in lines 18-21 in an efficient way, and hiding it neatly
# under the surface

# what happens if you try to retrieve an item that is not in the dictionary?
# what happens if you try to access a dictionary item using it's order, a number, like you do with a list

# you add entries to a dictionary like this:
na_city_populations_dict['Champaign'] = 87432

# so just like a list, you can start with an empty list, dict = {}, and add things one at a time

# here are some operators for dictionaries (or things you can do to them, as in + is an operator for an integer,
# a thing you can do to it. print them out so they make sense to you
# dictionary size
num_cities = len(na_city_populations_dict)

# remove a key from dictionary
del na_city_populations_dict['Los Angeles']

# check to see if a key is in a dictionary
if 'Los Angeles' in na_city_populations_dict:
    in_dictionary = True
else:
    in_dictionary = False

# retrieve a key's value if the key is in the dictionary
# test it out with some city names. what does it do if you type a city not in the dictionary
print(na_city_populations_dict)
city_input = input('Type a city name: ')
print(na_city_populations_dict.get(city_input))

# write a program that takes last week's test_file2.txt as input (the file with the animals and where they are from
# and put's each animal into the dictionary as a key, with the location as it's value. Then write a look that iterates
# through the whole dictionary, printing them out one at a time.
