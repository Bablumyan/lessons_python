"""List items are ordered, changable, allow duplicate values, indexed."""
print("Start")
this_list=["apple","orange","banana","cherry", "Orange",]
print(this_list)
print(type(this_list))
print(len(this_list))

second_this_list = ["abs",125, True, 15.32, "jkhk"]
print(second_this_list)
print(type(second_this_list))

construct_list = list(("apple","cherry"))
print(construct_list)
print(type(construct_list))

print(this_list[1])     #possitive index
print(this_list[-1])    #negative index - return last value of the list(for -1)

#Range of indexes
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango","melon"]
print(fruits[3:5])
print(fruits[0:5])
print(fruits[3:])
print(fruits[2:-2])

""" Check if item exist """
if "melon" in fruits:
    print("Yes, there is a melon fruit in the list")

""" Change item value """
cars = ["Mercedes","BMW", "AUDI"]
cars[1] = "Volvo"
print(cars)

cars[1:3] = ["blackcurrant", "Hundai"]
print(cars)

cars.append("Kia")
print(cars)

cars.insert(2,"Skoda")
print(cars)
