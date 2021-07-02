"""Tuple items are ordered, not changable, allow duplicate values"""
print("tuple")
brands = ("BMW", "AUDI", "SUBARU")
change = list(brands)
change.append("Toyota")
brands = tuple(change)
print(brands)
print(type(brands))


n_tuple = (1, 1, [3,4])
print(n_tuple)
n_tuple[2].append(5)
print(n_tuple)

brands = tuple(change)
val = ('data science', 'python',)    #, '9.6.5'
val_in_list = list(val)
print(type(val_in_list))


print(type(val))
#'tuple' object does not support item assignment
flds = ('Cource', 'Technology')   #, 'Version'

"""
all_inf = flds(val)
print(all_inf)
"""

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])
x = tup2.count(3)
print(x)

