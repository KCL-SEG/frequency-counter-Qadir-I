"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
#test
def frequencies(items):
    frequencies = {}
    # Your code goes here
    for x in items:
    #converting to string
        key = str(x)
        #adding new key and initialising to 0, increment run after if statement
        if key not in frequencies:
            frequencies[key] = 0
        frequencies[key] += 1
    return frequencies
    
