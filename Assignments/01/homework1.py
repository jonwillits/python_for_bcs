"""Homework 1
"""
'''
    0. What is the difference between a list and a tuple? What is a situation you might want to use a tuple instead
    of a list? (1 POINTS)
'''
a0 = "your answer to question 0"
print(a0 + "\n\n")

'''
    1. The lab for_loops.py described two ways of writing for loops. How were they different? What are the advantages
    of each way of doing it? (1 POINTS)
'''
a1 = "your answer to question 1"
print(a1 + "\n\n")

'''
    2. what do "break" and "continue" do in loops? (1 POINTS)
'''
a2 = "your answer to question 2"
print(a2 + "\n\n")

'''
    3. what is a list "slice"? How do you slice a list, and what is the result? (1 POINTS)
'''
a3 = "your answer to question 3"
print(a3 + "\n\n")


'''
    4. There are a bunch of useful things you can do with lists. write code that prints out the result after doing the 
    following things to the lists below: (5 POINTS)
    a) sort them
    b) get their sizes
    c) concatenate them
    d) get the count of a particular item in a list
    e) remove the duplicates from a list
'''
list_a = [1, 2, 3, 4, 5, 6]
list_b = ["dog", "cat", "lion", "tiger", "rat", "mouse", "rat", "mouse"]
print("answer to 4a")
print("answer to 4b")
print("answer to 4c")
print("answer to 4d")
print("answer to 4e")

'''
5. A string can be treated like a list. Write code that that uses the input function to take in a string, and
save it to a variable. Then write a for loop that prints out each letter in the string, one by one. (2 POINTS)
'''
print("answer to question 5\n\n")


'''
6. Strings have a method  called .split(). When applied to a string, it returns a list, as shown below. Write code that:
    - creates a second list called "type_list" that has all duplicates from first list removed
    - print out the type_list
    - has a for loop that iterates over each item in "type_list", prints out that word, and prints out how many times it 
      occurs in "token_list", the result should look something like:
      i: 2
      am: 2
      the: 3
      egg: 2
      man: 1
      ...
    
    As with all homework questions, you are welcome to find and use code on the internet that does this, as long as you 
    understand how it works. Make sure you comment the code and explain how it works, so that we know you understand it.
(3 POINTS)
'''

input_string = "i am the egg man. they are the egg men. i am the walrus. goo goo g'joob."
token_list = input_string.split(" ")
print(token_list)


'''
7. You can make a list out of anything, even other lists. Write code that takes in input from the keyboard, and adds
each word to a list. If the list is three items long, add that list as an element to a "master_list". For example, 
if the words "one" through "nine" were typed at the keyboard, the resulting "master_list" should be:
master_list = [["one", "two", "three"], ["four", "five", "six"], ["seven", "eight", "nine"]]

As with all homework questions, you are welcome to find and use code on the internet that does this, as long as you 
understand how it works. Make sure you comment the code and explain how it works, so that we know you understand it.
(3 POINTS)
'''
master_list = []
# your code to #7 goes here
print(master_list)


'''
8. Correctly complete the code for lab4_big5e2.py. Do NOT paste the code here, we will check your answer in that file.
(4 POINTS)
'''