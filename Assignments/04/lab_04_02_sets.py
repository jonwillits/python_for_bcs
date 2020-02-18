
# sets are like lists, except that you cant have duplicates.
my_set = set()

# you can add items easily
my_set.add('lion')
my_set.add('tiger')
my_set.add('bear')
# add some more animals to your set. make sure you try to add a duplicate and see what happens

# hear are some other functions you can do with a set. test them and see what they do, and explain in the comments
my_set.discard()
my_set.remove()
my_set.copy()
my_set.clear()
my_set.union()
my_set.intersection()
my_set.difference()
my_set.difference_update()
my_set.isdisjoint()
my_set.issubset()
my_set.issuperset()

# explain what happens here:
my_set = set("abcdefghijklmnopqrstuvwxyz")
my_set = set(['a', 'b', 'c'])