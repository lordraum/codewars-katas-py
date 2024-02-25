# Convert a string to an array
# Write a function to split a string and convert it into an array of words
# Example "Robin Singh" ==> ["Robin", "Singh"]

#def stringToArray(s):
    #return  s.split(' ')

from ast import Lambda


stringToArray = lambda s: s.split(' ')

print(stringToArray("Robin Singh"))