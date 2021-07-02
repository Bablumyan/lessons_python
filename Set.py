from typing import Union


this_set = {"apple","banana","orange","apple","kiwi"}
print(this_set)

for i in this_set:
    pass
print("orange" in this_set)

"""methods"""
#add
this_set = {"apple","banana","orange","apple","kiwi"}
this_set.add("graipfruit")
print(this_set)

#update(extand)
additional_set_1 = {"a","b","c"}
additional_set_2 = ["d","e","f","g"]
additional_set_1.update(additional_set_2)
print("-update-")
print(additional_set_1)
print(additional_set_2)

#remove
additional_set_1.remove("a")    #remove() method raises an error when the specified element doesn't exist in the given set
print("remove")
print(additional_set_1)
additional_set_1.discard("f")   #discard() method does not raises an error when the specified element doesn't exist in the given set
print("discard")
print(additional_set_1)

#pop    remove last value
print("pop")        
example_for_pop = {"BMW","AUDI","KIA"}
example_for_pop.pop()
print(example_for_pop)

#union
set_1 = {"x","y","z"}
set_2 = {1,2,3}
set_3 = set_1.union(set_2)
print("union")
print(set_3)

#intersection_update(), in intersection case the additional value will get the result
intersect_join_1 = {"a","v","h","i"}
intersect_join_2 = {"a","b","c","i"}
intersect_join_3 = intersect_join_1.intersection(intersect_join_2)
intersect_join_1.intersection_update(intersect_join_2)
print(intersect_join_1)
print(intersect_join_3)

#symmetric_difference_update()--Extand
first_set= {"apple", "banana", "cherry"}
second_set= {"google", "microsoft", "apple"}
first_set.symmetric_difference_update(second_set)

print(first_set)

#same for without "#_update"





