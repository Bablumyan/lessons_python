"""Extend list"""
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango","melon","apple", "manana"]
troppical_fruits = ["mango","pineapple","papaya"]
fruits.extend(troppical_fruits)
print(fruits)

"""remove specified item"""
fruits.remove("apple")
print(fruits)

""" remove specified index"""
fruits.pop(2)
print(fruits)

""" del 
del troppical_fruits
print(troppical_fruits)
"""

fruits.clear()
print(fruits)